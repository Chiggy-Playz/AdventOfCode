from contextlib import contextmanager
from time import perf_counter_ns
from typing import Generator


def format_time(time_value: float, is_ns: bool = False) -> str:

    # Convert from ns to seconds if needed
    if is_ns:
        time_value /= 1e9

    # Conversion thresholds
    if time_value < 1e-6:  # Less than 1 microsecond
        return f"{time_value * 1e9:.2f} ns"
    elif time_value < 1e-3:  # Less than 1 millisecond
        return f"{time_value * 1e6:.2f} µs"
    elif time_value < 1:  # Less than 1 second
        return f"{time_value * 1e3:.2f} ms"
    elif time_value < 60:  # Less than 1 minute
        return f"{time_value:.2f} s"
    elif time_value < 3600:  # Less than 1 hour
        minutes = int(time_value // 60)
        seconds = time_value % 60
        return f"{minutes} min {seconds:.2f} s"
    else:  # 1 hour or more
        hours = int(time_value // 3600)
        minutes = int((time_value % 3600) // 60)
        seconds = time_value % 60
        return f"{hours} hr {minutes} min {seconds:.2f} s"


@contextmanager
def timeit(message: str) -> Generator[None, None, None]:
    start = perf_counter_ns()
    yield
    diff = perf_counter_ns() - start
    print(f"{message} took {format_time(diff, is_ns=True)}")