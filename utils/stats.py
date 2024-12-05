import sys
import time
from timeit import timeit
from typing import Callable

from .timing import format_time
from .types import InputType


def silent_main(main: Callable, lines: InputType):
    # Capture and discard output
    old_stdout = sys.stdout
    sys.stdout = open("/dev/null", "w") if sys.platform != "win32" else open("NUL", "w")
    try:
        main(lines)
    finally:
        sys.stdout = old_stdout


def benchmark(main: Callable, lines: InputType, number: int = 100):

    # Benchmark the main function
    start_total = time.perf_counter()

    # Use timeit for precise measurement
    total_time = timeit(lambda: silent_main(main, lines), number=number)

    end_total = time.perf_counter()
    total_wall_time = end_total - start_total

    # Detailed time measurements
    print("\n--- Benchmarks ---")
    print(f"Number of runs: {number}")
    print(f"Average per run: {format_time(total_time / number)}")

    return total_wall_time
