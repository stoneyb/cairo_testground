#!/usr/bin/env python

import cairocffi as cairo

WIDTH, HEIGHT = 512, 512

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)

ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas

pat = cairo.SolidPattern(1, 1, 1, 1) # White

ctx.rectangle (0, 0, 1, 1) # Rectangle(x0, y0, x1, y1)
ctx.set_source (pat)
ctx.fill ()

ctx.translate (0.1, 0.1) # Changing the current transformation matrix

end = 0.8
start_step = 0
ctx.move_to(0, start_step)
ctx.line_to(end, start_step)  # Line to (x,y)

def cantor(step, start, line_len):
    step += 0.05
    if step > 0.5: return
    # Draw two lines
    # Line one
    ctx.move_to(start, step)
    ctx.line_to(start + line_len / 3, step)  # Line to (x,y)
    # Line two
    ctx.move_to(start + 2 * line_len / 3, step)
    ctx.line_to(start + line_len, step)  # Line to (x,y)
    # Next line
    cantor(step, start, line_len / 3)
    cantor(step, start + 2 * line_len / 3, line_len / 3)

cantor(start_step, 0, end)


ctx.set_source_rgb (0.3, 0.2, 0.5) # Solid color
ctx.set_line_width (0.005)
ctx.stroke()

surface.write_to_png ("img/cantor.png") # Output to PNG
