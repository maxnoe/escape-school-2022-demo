from functools import cache
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
from matplotlib.collections import PatchCollection
import numpy as np

__all__ = [
    'fibonacci',
    'fibonacci_generator',
    'fibonacci_tiling',
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
    x_cent = 0
    y_cent = 0
    angle = 180
    prev_length = 0

    rectangles = []
    for i, length in enumerate(fibs[1:]):
        rectangles.append(Rectangle((x,y), length, length))

        if i % 4 == 0:
            x_cent = x + length
            y_cent = y + length
            x += length
        if i % 4 == 1:
            x_cent = x
            y_cent = y + length
            x -= prev_length
            y += length
        if i % 4 == 2:
            x_cent = x
            y_cent = y
            x -= length + prev_length
            y -= prev_length
        if i % 4 == 3:
            x_cent = x + length
            y_cent = y
            y -= length + prev_length

        prev_length = length
        arc = (Arc(xy=(x_cent,y_cent), width=2*length, height=2*length, theta1=0, theta2=90, angle=angle))
        ax.add_patch(arc)
        angle += 90

    p = PatchCollection(rectangles)
    p.set(array=np.arange(n + 1), cmap='inferno', alpha=0.5)


    ax.set_axis_off()
    ax.add_collection(p)
    ax.set_aspect(1)
    ax.autoscale()
    ax.margins(0)
    plt.show()



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
