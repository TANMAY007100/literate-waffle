import turtle as te

# Initialize screen
screen = te.Screen()
# The width:height ratio is 3:5
width = 1000
height = 600
screen.setup(width, height)

flag_background = te.Turtle()
flag_background.color("#006a4e","#006a4e")
flag_background.begin_fill()
flag_background.setpos(0, 0)
flag_background.forward(width / 2)
flag_background.right(90)
flag_background.forward(height / 2)
flag_background.right(90)
flag_background.forward(width)
flag_background.right(90)
flag_background.forward(height)
flag_background.right(90)
flag_background.forward(width)
flag_background.right(90)
flag_background.forward(height / 2)
flag_background.end_fill()
flag_background.hideturtle()

red_circle = te.Turtle()
red_circle.color("#f42a41","#f42a41")
red_circle.penup()
x = (5 / 100) * width
radius = 0.2 * width
red_circle.right(180)
red_circle.forward(x)
radial_point = red_circle.pos()
red_circle.left(90)
red_circle.forward(radius)
red_circle.left(90)
red_circle.pendown()
red_circle.begin_fill()
red_circle.circle(radius)
red_circle.end_fill()
red_circle.hideturtle()
# Main Loop
te.done()