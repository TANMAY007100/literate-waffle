import turtle as te

screen_width = 2056
screen_height = 1329

# Initialize screen
screen = te.Screen()
# The width:height ratio is 5:3
flag_width = 1000
flag_height = 600

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# TODO Make screen_height and screen_width values taken from actual screen.
screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

flag_turtle = te.Turtle()
flag_turtle.color("#006a4e","#006a4e")
flag_turtle.begin_fill()
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
red_circle.color("#f42a41","#f42a41")
red_circle.penup()
radius = 0.2 * flag_width
circle_center_x = ((45 / 100) * flag_width) - (flag_width / 2)
circle_center_y = (flag_height / 2) - (flag_height / 2)
red_circle.setpos(circle_center_x, circle_center_y)
red_circle.right(90)
red_circle.forward(radius)
red_circle.left(90)
red_circle.pendown()
red_circle.begin_fill()
red_circle.circle(radius)
red_circle.end_fill()
red_circle.hideturtle()

# Main Loop
te.done()