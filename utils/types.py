from typing import TypeVar, TypeAlias, Union

Num = Union[int, float]  # Number type
InputType = TypeVar("InputType", str, list[str])
Point: TypeAlias = tuple[Num, Num]
LPoints: TypeAlias = list[Point]
SPoints: TypeAlias = set[Point]
Points: TypeAlias = Union[LPoints, SPoints]

# Define a Grid type that can be a 1D list of T (list[str] or list[int]),
# or a 2D list of T (list[list[str]] or list[list[int]])
T = TypeVar("T", str, int)
Grid = Union[list[T], list[list[T]]]
