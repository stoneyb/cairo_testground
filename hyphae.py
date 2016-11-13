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


def circle(ctx, x, y, r, color=[1, 0, 0]):
    ctx.arc(x, y, r, 0, 2.0 * math.pi)
    ctx.set_source_rgb(*color)
    ctx.fill()


def random_circle(ctx, r):
    rx = random.randint(0, WIDTH)
    ry = random.randint(0, HEIGHT)
    circle(ctx, rx, ry, r)


def random_points(num, size=WIDTH):
    return np.random.uniform(0, size, size=(num, 2))


def distance_between(pt1, pt2):
    return math.hypot(pt2[0] - pt1[0], pt2[1] - pt1[1])  # Linear distance


def angle_between(pt1, pt2, degrees=False):
    dx = pt1[0] - pt2[0]
    dy = pt1[1] - pt2[1]
    rads = abs(math.atan2(dy, dx))

    if degrees:
        return math.degrees(rads)
    return rads


def main():
    surface, ctx = initialize()
    max_radius = 0.01 * WIDTH # max radius

    # for i in range(HEIGHT):
    #     circle(ctx, WIDTH / 2., HEIGHT - (i), max_radius - i * 50.0 / float(HEIGHT))

    # Where HEADs grow towards
    nodes = random_points(3)

    for i in range(len(nodes)):
        circle(ctx, nodes[i][0], nodes[i][1], max_radius)

    # The inital starting locations
    auxin = [[WIDTH/2., HEIGHT]]

    # Current branches, at start consists of auxin
    heads = list(auxin)
    for itr in range(1000):
        print nodes
        head_nodes = {}
        to_kill = None
        # For each node find closest HEAD
        for i in range(len(nodes)):
            min = float("inf")
            closest = -1
            for h_idx, h in enumerate(heads):
                distance = distance_between(nodes[i], h)
                if distance < 100:
                    # kill node
                    to_kill = i
                if distance < min:
                    min = distance
                    closest = h_idx
            # Add node to collection for HEAD
            if not head_nodes.has_key(closest):
                head_nodes[closest] = [nodes[i]]
            else:
                head_nodes[closest].append(nodes[i])
        # Find average direction for head nodes and move
        for h_idx, nodes in head_nodes.items():
            directions = []
            for node in nodes:
                directions.append(angle_between(heads[h_idx], node))
            #print np.mean(directions)
            #print map(math.degrees, directions)
            #print math.degrees(np.mean(directions))
            # Move HEAD
            cx = heads[h_idx][0]
            cy = heads[h_idx][1]
            #print cx, cy
            r = 10
            x = cx - r * math.cos(np.mean(directions))
            y = cy - r * math.sin(np.mean(directions))
            circle(ctx, x, y, r, color=[0, 0, 0])
            #print x, y
            heads = [[x, y]]

        if to_kill:
            print 'kill'
            nodes = np.delete(nodes, to_kill, 0)
            print nodes

        if heads[0][0] < 0 or heads[0][0] > WIDTH or heads[0][1] < 0 or heads[0][1] > HEIGHT:
            print itr
            print nodes
            break

    for i in range(len(nodes)):
        circle(ctx, nodes[i][0], nodes[i][1], max_radius, color=[0, 1, 0])

    write_file('img/hyphae.png', surface)

if __name__ == '__main__':
    main()
