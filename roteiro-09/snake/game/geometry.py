"""Tipos de dados imutáveis para geometria do tabuleiro."""
from __future__ import annotations

from enum import Enum
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class BoardSize(NamedTuple):
    width: int
    height: int


def add(point: Point, delta: Point) -> Point:
    return Point(point.x + delta.x, point.y + delta.y)


def wrap(point: Point, board: BoardSize) -> Point:
    """Espaço toroidal: atravessar uma borda leva à borda oposta."""
    return Point(point.x % board.width, point.y % board.height)


class Direction(Enum):
    NORTH = Point(0, -1)
    SOUTH = Point(0, 1)
    EAST = Point(1, 0)
    WEST = Point(-1, 0)

    @property
    def delta(self) -> Point:
        return self.value


_OPPOSITE = {
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
    Direction.EAST: Direction.WEST,
    Direction.WEST: Direction.EAST,
}


def opposite(direction: Direction) -> Direction:
    return _OPPOSITE[direction]
