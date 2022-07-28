from drawingpanel import *

height = 1000
width = 1000
panel  = DrawingPanel(width, height)
panel.set_background("white")
canvas = panel.canvas


def main():
	count = 1
	text = "HELLO"
	while True:
		#if count % 2 == 1:
		canvas.create_text(500, 150, text=text, fill="black", font=('Helvetica 15 bold'))
		#else:
		text = text + "O"
		#	canvas.create_text(500, 150, text= text, fill="black", font=('Helvetica 15 bold'))
		panel.sleep(60)
		canvas.delete('all')
		count += 1

	panel.mainloop()

main()


