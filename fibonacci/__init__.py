from functools import cache
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import numpy as np

@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_tiling(n):
    fibs = [fibonacci(i) for i in range(n)]

    fig, ax = plt.subplots()

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


    p = PatchCollection(rectangles, cmap=matplotlib.cm.jet, alpha=0.4)
    p.set(array=np.asarray(range(n + 1)), cmap=matplotlib.cm.jet)
    ax.add_collection(p)

    plt.autoscale()
    plt.show()

