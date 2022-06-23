from functools import cache
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import numpy as np
import turtle

__all__ = [
    'fibonacci',
    'fibonacci_generator',
    'fibonacci_tiling',
    'fibonacci_word',
    'fibonacci_fractal',
]

@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_tiling(n):
    fibs = [fibonacci(i) for i in range(n+1)]

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    x = 0
    y = 0
    prev_length = 0

    rectangles = []
    for i, length in enumerate(fibs[1:]):
        rectangles.append(Rectangle((x,y), length, length))

        if i % 4 == 0:
            x += length
        if i % 4 == 1:
            x -= prev_length
            y += length
        if i % 4 == 2:
            x -= length + prev_length
            y -= prev_length
        if i % 4 == 3:
            y -= length + prev_length

        prev_length = length


    p = PatchCollection(rectangles)
    p.set(array=np.arange(n + 1), cmap='inferno')

    ax.set_axis_off()
    ax.add_collection(p)
    ax.set_aspect(1)
    ax.autoscale()
    ax.margins(0)
    plt.show()


def fibonacci_word(n):
    w0 = np.array([False])
    word = np.array([False,True])
    for i in range(2, n + 1):
        tmp = word
        word = np.append(word,w0)
        w0 = tmp
    return word

def fibonacci_fractal(n):
    word = fibonacci_word(n)
    s = turtle.getscreen()
    t = turtle.Turtle()
    for i, w in enumerate(word):
        t.forward(5)
        if w == False:
            if i % 2 == 0:
                t.left(90)
            else:
                t.right(90)

    turtle.done()

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
