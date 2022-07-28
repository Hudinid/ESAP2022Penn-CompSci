import turtle

def tree(length, level, my_turtle, angle):
	#my_turtle unchanged during recursive calls.
	#length controls the current length of tree
	#higher the level, the smaller the length
	my_turtle.pd()
	#the upper levels are green
	if level > 3:
		my_turtle.color('green')
	else:
		my_turtle.color('brown')

  #base_case
	if length < 50:
		return 
	else:
		my_turtle.forward(length)
		#turn right angle deg
		my_turtle.right(angle)
		#make a smaller tree at 20 degree angle relative to curr pos
		tree(length - 20, level + 1, my_turtle, angle)
		#
		my_turtle.left(angle)
		tree(length - 20, level + 1, my_turtle, angle)
		my_turtle.left(angle)
		tree(length - 20, level + 1, my_turtle, angle)
		#go back to the original orientation
		my_turtle.right(angle)
		my_turtle.pu()
		my_turtle.backward(length)

	

def main():
	wn = turtle.Screen()
	t = turtle.Turtle()
	t.speed(10)
	#do down 250 pixels
	t.pu() #pen up
	t.left(90)
	t.backward(250)
	t.pd()
	t.width(5)
	t.color('brown')

	tree(150, 0, t, 20)

	wn.bgcolor("cyan")

	wn.exitonclick()

main()



