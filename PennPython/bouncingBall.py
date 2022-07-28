from drawingpanel import *
import random

width = 600
height = 600
panel = DrawingPanel(width, height)
panel.set_background("white")
canvas = panel.canvas

class Ball():
    def __init__(self, ball_color, posX, posY, radius, vx, vy):
        self.ball_color = ball_color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.trail = []
        self.tailLength = 3

    def update(self):
        self.posX += self.vx
        self.posY += self.vy
        self.vy += 5

    def draw(self):
        newBall = canvas.create_oval(self.posX - self.radius, self.posY - self.radius
        , self.posX + self.radius,
		self.posY + self.radius,
        fill = self.ball_color)
        return newBall

    def check_for_bounce(self):
        if self.posX >= width-self.radius-5 or self.posX <= 0 + self.radius+5:
            self.vx *= -1
        if self.posY >= height-self.radius-5 or self.posY <= 0+self.radius+5:
            self.vy -= random.randint(3, 5)
            self.vy *= -1

    def randomColor(self):
        lst = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        return random.choice(lst)

    def create_trail(self):
        if len(self.trail) == self.tailLength:
            canvas.delete(self.trail[self.tailLength-1])
            del self.trail[self.tailLength - 1]
            newCircle = canvas.create_oval(self.posX - self.radius, self.posY - self.radius, self.posX + self.radius,
            self.posY + self.radius, fill = self.randomColor())
            self.trail.insert(0, newCircle)
        else:
            newCircle = canvas.create_oval(self.posX - self.radius, self.posY - self.radius, self.posX + self.radius,
            self.posY + self.radius, fill = self.randomColor())
            self.trail.insert(0, newCircle)

    def check_collision(self, apple, appleDrawing):
        x = self.posX - apple.posX #distance calculations
        y = self.posY - apple.posY
        c = (x**2 + y**2) ** 0.5

        # print(c)
        if c <= 40:
            self.tailLength += 1
            canvas.delete(appleDrawing)
            print("HELLO")
            return True

        return False

    def draw_new_apple(self):
        x = random.randint(200, 500)
        y = random.randint(200, 500)
        radius = 15
        apple = Ball("red", x, y, radius, 0, 0)

        return apple


def main():
    ball = Ball("green", 100, 400, 8, vx = 22, vy = -36)
    apple = ball.draw_new_apple()
    apple_drawing = apple.draw()
    count = 0
    while True:
        newBall = ball.draw()
        ball.update()
        ball.check_for_bounce()
        panel.sleep(30)

        if ball.check_collision(apple, apple_drawing):
            apple = ball.draw_new_apple()
            apple_drawing = apple.draw()


        if(count % 2 == 0): # changing the 2 will change how fast the tail is created
            ball.create_trail()
        count += 1
        canvas.delete(newBall) #deletes old ball instance
main()
