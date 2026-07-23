"""Casca imperativa: terminal (blessed), tempo, aleatoriedade e o loop do jogo.

Esta é a única parte do programa com efeitos colaterais. Ela orquestra o
núcleo funcional (core.py, render.py, history.py), mas nunca o contrário:
nada em game/core.py, game/render.py ou game/history.py sabe que blessed,
time ou random existem.
"""
from __future__ import annotations

import random
import time
from typing import Optional

from blessed import Terminal

from .commands import Command, parse_key
from .core import advance, initial_state, quit_game, turn
from .geometry import BoardSize
from .history import History, record
from .render import render_frame
from .state import GameState, Status

BOARD = BoardSize(width=40, height=20)
REPLAY_FRAME_DELAY = 0.04


def key_name(key) -> str:
    """Converte uma Keystroke do blessed no nome usado por commands.parse_key."""
    if key.is_sequence:
        return key.name or ""
    return str(key)


def apply_key(state: GameState, name: str) -> GameState:
    """Interpreta uma tecla monadicamente: chave desconhecida não altera o estado."""
    return (
        parse_key(name)
        .map(lambda command: quit_game(state) if command is Command.QUIT else turn(state, command))
        .unwrap_or(state)
    )


def draw(term: Terminal, frame) -> None:
    output = term.home + term.clear + "\r\n".join(frame)
    print(output, end="", flush=True)


def terminal_too_small(term: Terminal) -> bool:
    return term.width < BOARD.width + 2 or term.height < BOARD.height + 4


def game_loop(term: Terminal, board: BoardSize, choice) -> tuple[GameState, History]:
    state = initial_state(board, choice)
    history: History = record((), state)

    while state.status is Status.RUNNING:
        draw(term, render_frame(state))
        key = term.inkey(timeout=state.speed)
        if key:
            state = apply_key(state, key_name(key))
        if state.status is not Status.RUNNING:
            break
        state = advance(state, choice)
        history = record(history, state)

    return state, history


def play_replay(term: Terminal, history: History) -> None:
    for state in history:
        draw(term, render_frame(state))
        time.sleep(REPLAY_FRAME_DELAY)
    print("\r\n Fim do filme. Pressione qualquer tecla para sair.", end="", flush=True)
    term.inkey()


def run() -> None:
    term = Terminal()

    if terminal_too_small(term):
        print(
            f"Terminal muito pequeno. Precisa de ao menos "
            f"{BOARD.width + 2}x{BOARD.height + 4}, "
            f"tem {term.width}x{term.height}."
        )
        return

    rng = random.Random()

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        _final_state, history = game_loop(term, BOARD, rng.choice)
        play_replay(term, history)
