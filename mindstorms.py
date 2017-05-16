import turtle

# course practice code
def draw_square(pad):
	for i in range(4):
		pad.forward(100)
		pad.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	# turtle is a class and pad and angie is object 
	pad = turtle.Turtle()
	pad.shape("turtle")
	for j in range(360/10):
		pad.right(10)
		draw_square(pad)
	pad.right(90)
	pad.forward(250)
	
	# angie = turtle.Turtle()
	# angie.color("black")
	# angie.shape("arrow")
	# angie.circle(100)
	window.exitonclick()

draw_art()


