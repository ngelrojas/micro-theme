import pytest
from datetime import datetime, timedelta
from typing import Callable


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"\n runtine: {diff.total_seconds()}")


class PerformanceExecption(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validate_runtime(*args, **kw):
        tick = datetime.now()
        result = method(*args, **kw)
        tock = datetime.now()
        runtime = tock - tick
        print(f"\n runtime: {runtime.total_seconds()}")

        if runtime > runtime_limit:
            raise PerformanceExecption(runtime=runtime, limit=runtime_limit)

        return result

    return run_function_and_validate_runtime
