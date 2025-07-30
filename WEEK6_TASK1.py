import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def example_function(n):
    total = sum(range(n))
    return total

example_function(1000000)
