import turtle as te


screen_width = 2056
screen_height = 1329

# Initialize screen
screen = te.Screen()
# The width:height ratio is 3:2
flag_width = 1200
flag_height = 800

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# TODO Make screen_height and screen_width values taken from actual screen.
screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

flag_turtle = te.Turtle()
flag_turtle.speed("fastest")
flag_turtle.color("#000000","#FFFFFF")
flag_turtle.penup()
flag_turtle.setpos(left_top_x, left_top_y)
flag_turtle.pendown()
flag_turtle.forward(flag_width)
flag_turtle.right(90)
flag_turtle.forward(flag_height)
flag_turtle.right(90)
flag_turtle.forward(flag_width)
flag_turtle.right(90)
flag_turtle.forward(flag_height)
flag_turtle.end_fill()
flag_turtle.hideturtle()

red_circle = te.Turtle()
red_circle.color("#BE0028","#BE0028")
red_circle.begin_fill()
red_circle.dot((3 / 5) * flag_height)
red_circle.end_fill()
red_circle.hideturtle()

# Main Loop
te.done()