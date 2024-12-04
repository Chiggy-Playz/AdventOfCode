import inspect
from os.path import dirname, basename, join
from typing import Optional, overload, Literal

@overload
def get_input(full_path: Optional[str] = None, lines: Literal[True] = True, testing: bool = False) -> list[str]:
    ...

@overload
def get_input(full_path: Optional[str] = None, lines: Literal[False] = False, testing: bool = False) -> str:
    ...

def get_input(full_path: Optional[str] = None, lines=True, testing=False):
    full_path = full_path or inspect.stack()[1].filename
    with open(
        join(
            dirname(full_path),
            "inputs",
            basename(full_path).split(".")[0] + (".test" if testing else "") + ".txt",
        )
    ) as f:
        return [line.strip() for line in f.readlines()] if lines else f.read()
