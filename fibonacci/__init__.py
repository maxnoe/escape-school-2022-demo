from functools import cache

__all__ = [
    'fibonacci',
    'fibonacci_generator',
]

@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_generator(n):
    yield 0

    if n == 0:
        return

    yield 1

    if n == 1:
        return

    n0, n1 = 0, 1
    for _ in range(2, n):
        n0, n1 = n1, n0 + n1
        yield n1
