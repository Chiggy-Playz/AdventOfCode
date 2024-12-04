from contextlib import contextmanager
from time import monotonic_ns
from typing import Generator

@contextmanager
def timeit(message: str) -> Generator[None, None, None]:
    start = monotonic_ns()
    yield
    diff = monotonic_ns() - start
    
    unit = "ns"
    if diff >= 1e9:
        unit = "s"
        diff /= 1e9
    elif diff >= 1e6:
        unit = "ms"
        diff /= 1e6
    elif diff >= 1e3:
        unit = "µs"
        diff /= 1e3

    print(f"{message} took {diff:.2f}{unit}")
    