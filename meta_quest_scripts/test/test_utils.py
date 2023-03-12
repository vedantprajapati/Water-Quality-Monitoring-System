import pytest
import time
from ..utils import timeit

def test_timeit():
    
    @timeit
    def f():
        time.sleep(0.01)

    timer = f()[1]
    assert timer < 0.011 and timer >= 0.010