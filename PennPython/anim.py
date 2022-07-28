from drawingpanel import *

height = 1000
width = 1000
panel  = DrawingPanel(width, height)
panel.set_background("white")
canvas = panel.canvas

class Ball():
	def __init__(self, ball_color, positionx, positiony, radius
		, vx, vy):
		self.color = ball_color #make the color for this ball = ball_color
		self.positionx= positionx
		self.positiony = positiony
		self.radius = radius
		self.vx = vx
		self.vy = vy

	def update(self):
		self.positionx += self.vx

		self.positiony += self.vy

		self.vy += 5


	def draw(self):
		canvas.create_oval(self.positionx - self.radius,
			self.positiony - self.radius
			, self.positionx + self.radius,
			self.positiony + self.radius, fill = self.color)

class Tower():
	def __init__(self, initx, inity, width, height):
		self.initx = initx
		self.inity = inity
		self.width = width
		self.height = height

	def draw(self):
		#canvas.create_polygon(300, 250, 20, 30, 30, 40)
		canvas.create_polygon(self.initx, self.inity, self.initx + self.width, self.inity
			, self.initx + self.width, self.inity + self.height, self.initx, self.inity + self.height, fill="red")

	def update(self):
		self.height += 4

def main():
	#ball_color, positionx, positiony, radius, vx, vy
	ball = Ball("green", 100, 400, 8, vx = 22, vy = -36)
	ball.draw()
	tower = Tower(300, 250, 10, 10)
	tower.draw()

	while True:
		ball.draw()
		tower.draw()
		panel.sleep(50)
		#erase everything
		canvas.delete('all')
		ball.update()
		tower.update()

  #need this for drawing panel to work
	panel.mainloop()

main()
