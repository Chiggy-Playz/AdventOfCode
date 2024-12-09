"""
Utility Functions for Sequence and Grid Operations

This module provides utility functions for performing operations on sequences,
grids, and iterables. These include mapping functions (`lmap`, `tmap`), 
grid traversal (`traverse_grid`), point-wise operations (`pdiff`, `padd`), 
and general-purpose checks (`ingrid`).

Type Variables:
    - T: Generic input type.
    - U: Generic output type.
    - Num: Number type (int or float).
"""

import re
from typing import Callable, Generator, Iterable, Sequence, TypeVar, Union, cast

from utils.types import Num, Point

T = TypeVar("T")  # Input type
U = TypeVar("U")  # Output type


def lmap(func: Callable[[T], U], iterable: Iterable[T]) -> list[U]:
    """
    Applies a function to each item in an iterable and returns a list of results.

    Args:
        func (Callable[[T], U]): A function to apply to each item in the iterable.
        iterable (Iterable[T]): An iterable of items to process.

    Returns:
        list[U]: A list containing the results of applying the function to the items.
    """
    return list(map(func, iterable))


def tmap(func: Callable[[T], U], iterable: Iterable[T]) -> tuple[U, ...]:
    """
    Applies a function to each item in an iterable and returns a tuple of results.

    Args:
        func (Callable[[T], U]): A function to apply to each item in the iterable.
        iterable (Iterable[T]): An iterable of items to process.

    Returns:
        tuple[U, ...]: A tuple containing the results of applying the function to the items.
    """
    return tuple(map(func, iterable))


def ingrid(n: int, x: Num, y: Num) -> bool:
    """
    Checks if the coordinates (x, y) are within the bounds of an n x n grid.

    Args:
        n (int): Size of the grid (n x n).
        x (Num): X-coordinate.
        y (Num): Y-coordinate.

    Returns:
        bool: True if the coordinates are within bounds, otherwise False.
    """
    return 0 <= x < n and 0 <= y < n


def diff(t: Sequence[Num]) -> Num:
    """
    Computes the difference between the second and the first elements of a sequence.

    Args:
        t (Sequence[Num]): A sequence of two numbers.

    Returns:
        Num: The difference t[1] - t[0].

    Raises:
        IndexError: If the sequence does not contain at least two elements.
    """
    return t[1] - t[0]


def pdiff(*points: Point) -> Point:
    """
    Computes the point-wise differences between two points.

    Args:
        points (Sequence[Point]): Two points represented as sequences of tuples.

    Returns:
        Point: A tuple containing the differences along each dimension.

    Raises:
        ValueError: If more than two points are provided.
    """
    if len(points) != 2:
        raise ValueError("Only 2 points of 2 dim supported")

    return cast(Point, tmap(diff, zip(*points)))


def padd(*points: Point) -> Point:
    """
    Computes the point-wise sum of points.

    Args:
        points (Sequence[Point]): Points represented as sequences of tuples.

    Returns:
        Point: A tuple containing the sums along each dimension.
    """
    return cast(Point, tmap(sum, zip(*points)))


def traverse_grid(grid: Union[list[list[T]], list[str]]) -> Generator[tuple[int, int, T | str], None, None]:
    """
    Traverses a 2D grid and yields the coordinates (x, y) and the value at each cell.

    Args:
        grid (list[list[T]]): A 2D grid represented as a list of lists.

    Yields:
        tuple[int, int, T]: The x-coordinate, y-coordinate, and value at each cell.
    """
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield x, y, grid[y][x]


def ints(s: str, greedy: bool = True) -> list[int]:
    """
    Extracts all integers from a given string.

    Args:
        s (str): The input string.

    Returns:
        List[int]: A list of integers found in the string.
    """
    return [int(i) for i in re.findall(r"\d+" if greedy else r"\d", s)]
