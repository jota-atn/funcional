"""Monad Result (Ok | Err) para tratamento de erros sem exceções."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E")


@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T

    def map(self, f: Callable[[T], U]) -> "Ok[U]":
        return Ok(f(self.value))

    def bind(self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
        return f(self.value)

    def unwrap_or(self, _default: T) -> T:
        return self.value

    def is_ok(self) -> bool:
        return True


@dataclass(frozen=True)
class Err(Generic[E]):
    error: E

    def map(self, _f: Callable[[T], U]) -> "Err[E]":
        return self

    def bind(self, _f: Callable[[T], "Result[U, E]"]) -> "Err[E]":
        return self

    def unwrap_or(self, default: T) -> T:
        return default

    def is_ok(self) -> bool:
        return False


Result = Union[Ok[T], Err[E]]
