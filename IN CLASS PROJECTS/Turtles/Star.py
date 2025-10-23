import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(400,300)
turtle.title("Turtle Screen 2")

pen = turtle.Turtle()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(50)

pen.pendown()
pen.right(90)

pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)

turtle.done()