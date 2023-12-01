from os.path import dirname, basename, join
from typing import overload, Literal


@overload
def get_input(full_path: str, lines: Literal[True] = ...) -> list[str]:
    ...


@overload
def get_input(full_path: str, lines: Literal[False]) -> str:
    ...


def get_input(full_path: str, lines=True):
    with open(
        join(dirname(full_path), "inputs", basename(full_path).split(".")[0] + ".txt")
    ) as f:
        return f.readlines() if lines else f.read()
