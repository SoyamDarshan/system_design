"""
- Want to augment an object with additional functionality
- Do not want to rewrite or alter existing code (Open Closed Principle)
- Want to keep new functionality separate (Single Responsibility Principle)
- Need to be able to interact with existing stuctures

Two options

- Inherit form required object (if possible)
- Build a Decorator, which simply references the decorated object

Facilitate the additional behaviour to individual object without inheriting from them

"""
import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end - start) * 1000}ms')
        return result

    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123


if __name__ == "__main__":
    some_op()
    # time_it(some_op)()
