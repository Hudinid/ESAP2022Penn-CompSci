# * means everything
from drawingpanel import *

#global variables
width = 1024
height = 768
#make a window of a certain width, height
panel = DrawingPanel(width, height)
canvas = panel.canvas

def draw_h(x, y, size):
    #draw an H centered at (x,y) of a certain size
    canvas = panel.canvas
    #horizontal line of length = size
    #canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x - size / 2, y, x + size / 2, y)
    # 2 vertical lines
    canvas.create_line(x - size / 2, y + size / 2,
        x - size / 2, y - size /2)
    canvas.create_line(x + size / 2, y + size / 2,
                    x + size / 2, y - size / 2)


def draw_h_recur(n,  x,  y, size):
    #n controlling the recursion level. What is the smallest size H.
        if n == 0:
        	return

        #draw the central/main H
        panel.sleep(1000)

        draw_h(x, y, size)

        #now recursively make 4 smaller H trees
        x0 = x - size / 2
        y0 = y - size / 2
        x1 = x + size / 2
        y1 = y + size / 2

        #draw the pattern with these new parameters
        draw_h_recur(n - 1, x0, y0, size / 2)
        draw_h_recur(n - 1, x0, y1, size / 2)
        draw_h_recur(n - 1, x1, y0, size / 2)
        draw_h_recur(n - 1, x1, y1, size / 2)


def main():

    draw_h_recur(3, width / 2, height / 2, width / 4)


main()
