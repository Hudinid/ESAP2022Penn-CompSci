from drawingpanel import *

def simple_drawing():
	#construct a panel of width 640, height = 480
	panel = DrawingPanel(640, 480)
	panel.set_background("orange")
	#get the canvas from this window/panel
	canvas = panel.canvas
	canvas.create_oval(100, 100, 250, 250, fill = "lightgreen")
	# canvas.create_polygon(50, 50, 0, 0, 90, 200, fill = "blue")
	canvas.create_polygon(0, 0, 0, 100, 100, 100, fill = "blue")

def main():
	simple_drawing()

main()
