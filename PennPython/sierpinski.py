from drawingpanel import *

width = 800
height = 800

panel = DrawingPanel(width, height)
canvas = panel.canvas

panel.set_background("orange")


def draw_triangle(x1, y1, x2, y2, x3, y3):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = "blue")

# draw_triangle(400, 0, 800)
def draw_tri_recurse(n, x1, y1, x2, y2, x3, y3):
    print("yes")
    if n == 0:
        return

    draw_triangle((x1+x2) / 2, (y1+y2) /2 , (x1 + x3) / 2, (y1 + y3) / 2, (x2 + x3) / 2, y3)
    print("hi")
    draw_tri_recurse(n - 1, x1, y1, (x1+x2) / 2, (y1+y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2)

    draw_tri_recurse(n - 1, (x1 + x2) / 2, (y1 + y2) / 2, x2, y2, (x2 + x3) / 2, y3)

    draw_tri_recurse(n - 1, (x1 + x3) / 2, (y1 + y3) / 2, (x2 + x3) / 2, y3, x3, y3)

canvas.create_polygon(400, 0, 0, 800, 800, 800, fill = "yellow")

n = 5
draw_tri_recurse(n, 400, 0, 0, 800, 800, 800)
