#!/usr/bin/env python

import math
import cairocffi as cairo

WIDTH, HEIGHT = 512, 512

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)

ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas

pat = cairo.SolidPattern(1, 1, 1, 1) # White

ctx.rectangle (0, 0, 1, 1) # Rectangle(x0, y0, x1, y1)
ctx.set_source (pat)
ctx.fill ()

ctx.translate (0, 0) # Changing the current transformation matrix

ctx.move_to (0, 0)
ctx.line_to (0.25, 0) # Line to (x,y)

ctx.move_to (0.25, 0.25)
ctx.line_to (0.5, 0.25) # Line to (x,y)

ctx.move_to (0.5, 0.5)
ctx.line_to (0.75, 0.5) # Line to (x,y)

ctx.move_to (0.75, 0.75)
ctx.line_to (1, 0.75) # Line to (x,y)

ctx.set_source_rgb (0.3, 0.2, 0.5) # Solid color
ctx.set_line_width (0.005)
ctx.stroke()




surface.write_to_png ("example.png") # Output to PNG