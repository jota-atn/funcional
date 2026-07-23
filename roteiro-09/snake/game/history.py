"""Histórico imutável de estados, usado para o "filme" de replay (Desafio)."""
from __future__ import annotations

from typing import Tuple

from .state import GameState

History = Tuple[GameState, ...]


def record(history: History, state: GameState) -> History:
    """Anexa um estado ao histórico. Função pura: devolve uma nova tupla."""
    return (*history, state)
