from matplotlib import pyplot as plt
from threading import Thread
import time
import math
import matplotlib.pyplot as plt


def draw():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    j = 0
    i = 0
    x, y = [], []

    while True:
        x.append(math.radians(15 * j))
        y.append(int(math.sin(math.radians(15 * j)) * 60))

        ax.plot(x, y, color='b')

        fig.canvas.draw()

        fig.show()
        plt.pause(0.05)
        i += 1
        j += 1


if __name__ == '__main__':
    draw()
