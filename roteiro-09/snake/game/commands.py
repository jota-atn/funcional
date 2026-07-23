"""Comandos que o jogador pode emitir e seu parsing a partir de teclas."""
from __future__ import annotations

from enum import Enum, auto

from .result import Err, Ok, Result


class Command(Enum):
    GO_NORTH = auto()
    GO_SOUTH = auto()
    GO_EAST = auto()
    GO_WEST = auto()
    QUIT = auto()


_KEY_MAP = {
    "w": Command.GO_NORTH,
    "KEY_UP": Command.GO_NORTH,
    "s": Command.GO_SOUTH,
    "KEY_DOWN": Command.GO_SOUTH,
    "a": Command.GO_WEST,
    "KEY_LEFT": Command.GO_WEST,
    "d": Command.GO_EAST,
    "KEY_RIGHT": Command.GO_EAST,
    "q": Command.QUIT,
    "KEY_ESCAPE": Command.QUIT,
}


def parse_key(key_name: str) -> Result[Command, str]:
    """Traduz o nome de uma tecla em um Command, ou Err se desconhecida."""
    command = _KEY_MAP.get(key_name)
    if command is None:
        return Err(f"tecla não mapeada: {key_name!r}")
    return Ok(command)
