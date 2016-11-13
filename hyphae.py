#!/usr/bin/env python

import cairocffi as cairo
import math
import random
import numpy as np

WIDTH, HEIGHT = 1000, 1000


def initialize():
    """
    Setup context with WIDTH and HEIGHT and background color
    """
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    pat = cairo.SolidPattern(1, 1, 1, 1)  # White

    ctx.rectangle(0, 0, WIDTH, HEIGHT)  # Rectangle(x0, y0, x1, y1)
    ctx.set_source(pat)
    ctx.fill()

    return surface, ctx


def write_file(filename, surface):
    surface.write_to_png(filename)


def circle(ctx, x, y, r):
    ctx.arc(x, y, r, 0, 2.0 * math.pi)
    ctx.set_source_rgb(0.3, 0.2, 0.5)
    ctx.fill()


def random_circle(ctx, r):
    rx = random.randint(0, WIDTH)
    ry = random.randint(0, HEIGHT)
    circle(ctx, rx, ry, r)


def random_points(num, size=WIDTH):
    return np.random.uniform(0, size, size=(num, 2))


def distance_between(pt1, pt2):
    return math.hypot(pt2[0] - pt1[0], pt2[1] - pt1[1])  # Linear distance


def main():
    surface, ctx = initialize()
    max_radius = 0.01 * WIDTH # max radius

    # for i in range(HEIGHT):
    #     circle(ctx, WIDTH / 2., HEIGHT - (i), max_radius - i * 50.0 / float(HEIGHT))

    pts = random_points(10)  # 10 random points
    auxin = [[HEIGHT, WIDTH/2.]]  # bottom center

    for i in range(len(pts)):
        print distance_between(pts[i], auxin[0])

    write_file('img/hyphae.png', surface)

if __name__ == '__main__':
    main()
