import turtle

def draw_fourside(pad):
	pad.forward(50)
	pad.right(60)
	pad.forward(50)
	pad.right(120)
	pad.forward(50)
	pad.right(60)
	pad.forward(50)
	pad.right(120)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor("red")
	pad = turtle.Turtle()
	for i in range(360/10):
		pad.right(10)
		draw_fourside(pad)
	pad.right(90)
	pad.forward(200)

	window.exitonclick()

draw_flower()

