from functools import wraps
import time

def timeit(func):
    """A decorator function to measure the execution time of a function and print it to the console.

    Args:
    func (function): The function to be wrapped with the timeit decorator.

    Returns:
    function: A wrapped function that measures the execution time of the original function and prints it to the console.
    """
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        if func.__name__ == "draw_octave":
            print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        else:
            print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper