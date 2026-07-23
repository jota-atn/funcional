"""Estado imutável do jogo. Projetado para não admitir estados inválidos."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple

from .geometry import BoardSize, Direction, Point

INITIAL_SPEED = 0.22
MIN_SPEED = 0.06
SPEED_STEP = 0.94


class Status(Enum):
    RUNNING = auto()
    GAME_OVER = auto()
    QUIT = auto()
    WON = auto()


@dataclass(frozen=True)
class GameState:
    board: BoardSize
    snake: Tuple[Point, ...]  # cabeça é sempre snake[0]; nunca vazia
    direction: Direction
    fruit: Point
    score: int
    speed: float  # segundos por tick; menor = mais rápido
    status: Status


def speed_up(speed: float) -> float:
    return max(MIN_SPEED, speed * SPEED_STEP)
