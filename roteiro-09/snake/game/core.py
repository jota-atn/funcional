"""Núcleo funcional puro do jogo: só funções, sem I/O.

Toda transição de estado é uma função pura State -> State (ou usa o monad
Result quando a operação pode falhar). Nenhuma função aqui toca terminal,
relógio ou gerador de números aleatório diretamente: tudo que é
não-determinístico (posição da fruta) recebe a decisão já pronta via
injeção de uma função `choice`.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Callable, List, Tuple

from .commands import Command
from .geometry import BoardSize, Direction, Point, add, opposite, wrap
from .result import Err, Ok, Result
from .state import GameState, Status, speed_up

Choice = Callable[[List[Point]], Point]


def empty_cells(snake: Tuple[Point, ...], board: BoardSize) -> List[Point]:
    occupied = set(snake)
    return [
        Point(x, y)
        for x in range(board.width)
        for y in range(board.height)
        if Point(x, y) not in occupied
    ]


def place_fruit(
    snake: Tuple[Point, ...], board: BoardSize, choice: Choice
) -> Result[Point, str]:
    """Escolhe uma célula livre para a fruta. Err se o tabuleiro está cheio."""
    candidates = empty_cells(snake, board)
    if not candidates:
        return Err("tabuleiro cheio: não há espaço para nova fruta")
    return Ok(choice(candidates))


def initial_state(board: BoardSize, choice: Choice) -> GameState:
    cx, cy = board.width // 2, board.height // 2
    snake = (Point(cx, cy), Point(cx - 1, cy), Point(cx - 2, cy))
    fruit = place_fruit(snake, board, choice).unwrap_or(Point(0, 0))
    return GameState(
        board=board,
        snake=snake,
        direction=Direction.EAST,
        fruit=fruit,
        score=0,
        speed=0.22,
        status=Status.RUNNING,
    )


_COMMAND_DIRECTION = {
    Command.GO_NORTH: Direction.NORTH,
    Command.GO_SOUTH: Direction.SOUTH,
    Command.GO_EAST: Direction.EAST,
    Command.GO_WEST: Direction.WEST,
}


def turn(state: GameState, command: Command) -> GameState:
    """Aplica uma direção absoluta. Ignora reversão instantânea e o resto."""
    if state.status is not Status.RUNNING:
        return state
    new_direction = _COMMAND_DIRECTION.get(command)
    if new_direction is None or new_direction is opposite(state.direction):
        return state
    return replace(state, direction=new_direction)


def quit_game(state: GameState) -> GameState:
    return replace(state, status=Status.QUIT)


def _collided_with_self(body: Tuple[Point, ...]) -> bool:
    head, *rest = body
    return head in rest


def advance(state: GameState, choice: Choice) -> GameState:
    """Avança um tick do jogo: move a snake, trata fruta e colisão."""
    if state.status is not Status.RUNNING:
        return state

    new_head = wrap(add(state.snake[0], state.direction.delta), state.board)
    ate_fruit = new_head == state.fruit
    grown_body = (new_head,) + state.snake
    body = grown_body if ate_fruit else grown_body[:-1]

    if _collided_with_self(body):
        return replace(state, status=Status.GAME_OVER)

    if not ate_fruit:
        return replace(state, snake=body)

    grown_state = replace(
        state,
        snake=body,
        score=state.score + 1,
        speed=speed_up(state.speed),
    )
    fruit_result = place_fruit(body, state.board, choice)
    return fruit_result.map(
        lambda new_fruit: replace(grown_state, fruit=new_fruit)
    ).unwrap_or(replace(grown_state, status=Status.WON))
