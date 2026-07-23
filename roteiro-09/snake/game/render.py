"""Tradução pura de GameState para um quadro de texto (frame).

Continua sendo núcleo funcional: recebe um estado e devolve strings.
Quem efetivamente escreve essas strings no terminal é a casca (shell.py).
"""
from __future__ import annotations

from typing import Tuple

from .geometry import Point
from .state import GameState, Status

HEAD_CHAR = "@"
BODY_CHAR = "o"
FRUIT_CHAR = "*"
EMPTY_CHAR = " "

Frame = Tuple[str, ...]


def render_frame(state: GameState) -> Frame:
    width, height = state.board.width, state.board.height
    body_cells = set(state.snake[1:])
    head = state.snake[0]

    def cell_char(point: Point) -> str:
        if point == head:
            return HEAD_CHAR
        if point in body_cells:
            return BODY_CHAR
        if point == state.fruit:
            return FRUIT_CHAR
        return EMPTY_CHAR

    rows = [
        "".join(cell_char(Point(x, y)) for x in range(width))
        for y in range(height)
    ]

    border = "+" + "-" * width + "+"
    boxed_rows = [f"|{row}|" for row in rows]

    return (border, *boxed_rows, border, status_line(state))


def status_line(state: GameState) -> str:
    ticks_per_second = 1.0 / state.speed
    label = {
        Status.RUNNING: "jogando",
        Status.GAME_OVER: "GAME OVER",
        Status.QUIT: "encerrado",
        Status.WON: "VOCÊ VENCEU!",
    }[state.status]
    return (
        f" Pontuação: {state.score:<4} "
        f"Velocidade: {ticks_per_second:4.1f}/s  "
        f"[{label}]"
    )
