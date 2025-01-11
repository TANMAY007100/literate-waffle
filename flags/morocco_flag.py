import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Morocco"
BRIGHT_RED = "#C1272D"
PALM_GREEN = "#006233"

# The width:height ratio is 3:2
flag_width = 1000
flag_height = 666

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

screen_width = te.getcanvas().winfo_screenwidth()
screen_height = te.getcanvas().winfo_screenheight()


# Note: If your window doesn't come in front of all other programs when you run it please uncomment these lines.
# This might be due to bug in MacOS Sequoia or libraries installed with Python. Do note that this keeps the window...
# in front all the other windows stacked on top, and it doesn't minimize when clicking outside the window.
# Get Window info from current canvas
# rootwindow = screen.getcanvas().winfo_toplevel()
# Bring the turtle window to front of stack
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, int((screen_width / 2) - (canvas_width / 2)), int((screen_height / 2) - (canvas_height / 2)))

# Create the flag field
field = te.Turtle()
field.penup()
# field.speed("fastest")
field.setpos((left_top_x, left_top_y))
field.pendown()
field.color(BRIGHT_RED, BRIGHT_RED)
field.begin_fill()
field.seth(0)
field.forward(flag_width)
field.right(90)
field.forward(flag_height)
field.right(90)
field.forward(flag_width)
field.right(90)
field.forward(flag_height)
field.end_fill()
field.hideturtle()

radius = flag_width / 6
star = te.Turtle()

draw_five_pointed_star(star, 5, radius, 0, 0, PALM_GREEN, PALM_GREEN, 10)

pentagon = te.Turtle()
pentagon_radius = radius / 2
# pentagon.speed("fastest")
# Draw inner pentagon
pentagon.penup()
pentagon.setpos(-25, 40)
pentagon.pendown()
pentagon.color(BRIGHT_RED, BRIGHT_RED)
pentagon.begin_fill()
pentagon.forward(55)
pentagon.right(72)
pentagon.forward(55)
pentagon.right(72)
pentagon.forward(55)
pentagon.right(72)
pentagon.forward(55)
pentagon.right(72)
pentagon.forward(55)
pentagon.end_fill()
pentagon.hideturtle()


# Top Triangle 1
top_triangle = te.Turtle()
# top_triangle.speed("fastest")
# Draw inner triangle
top_triangle.penup()
top_triangle.setpos(0, 122)
top_triangle.pendown()
top_triangle.color(BRIGHT_RED, BRIGHT_RED)
top_triangle.seth(270)
top_triangle.begin_fill()
top_triangle.left(20)
top_triangle.forward(75)
top_triangle.right(110)
top_triangle.forward(50)
top_triangle.right(108)
top_triangle.forward(75)
top_triangle.end_fill()
top_triangle.hideturtle()

# Right top Triangle 2
right_top_triangle = te.Turtle()
# right_top_triangle.speed("fastest")
# Draw inner triangle
right_top_triangle.penup()
right_top_triangle.setpos(120, 40)
right_top_triangle.pendown()
right_top_triangle.color(BRIGHT_RED, BRIGHT_RED)
right_top_triangle.seth(180)
right_top_triangle.begin_fill()
right_top_triangle.forward(78)
right_top_triangle.left(108)
right_top_triangle.forward(45)
right_top_triangle.left(105)
right_top_triangle.forward(78)
right_top_triangle.end_fill()
right_top_triangle.hideturtle()


# Left top Triangle 3
left_top_triangle = te.Turtle()
# left_top_triangle.speed("fastest")
# Draw inner triangle
left_top_triangle.penup()
left_top_triangle.setpos(-120, 40)
left_top_triangle.pendown()
left_top_triangle.color(BRIGHT_RED, BRIGHT_RED)
left_top_triangle.seth(0)
left_top_triangle.begin_fill()
left_top_triangle.forward(78)
left_top_triangle.right(108)
left_top_triangle.forward(45)
left_top_triangle.right(105)
left_top_triangle.forward(78)
left_top_triangle.end_fill()
left_top_triangle.hideturtle()

# Left bottom Triangle 4
left_bottom_triangle = te.Turtle()
# left_bottom_triangle.speed("fastest")
# Draw inner triangle
left_bottom_triangle.penup()
left_bottom_triangle.setpos(-75, -101)
left_bottom_triangle.pendown()
left_bottom_triangle.color(BRIGHT_RED, BRIGHT_RED)
left_bottom_triangle.seth(70)
left_bottom_triangle.begin_fill()
left_bottom_triangle.forward(78)
left_bottom_triangle.right(108)
left_bottom_triangle.forward(45)
left_bottom_triangle.right(105)
left_bottom_triangle.forward(78)
left_bottom_triangle.end_fill()
left_bottom_triangle.hideturtle()

# Right bottom Triangle 5
right_bottom_triangle = te.Turtle()
# right_bottom_triangle.speed("fastest")
# Draw inner triangle
right_bottom_triangle.penup()
right_bottom_triangle.setpos(75, -101)
right_bottom_triangle.pendown()
right_bottom_triangle.color(BRIGHT_RED, BRIGHT_RED)
right_bottom_triangle.seth(108)
right_bottom_triangle.begin_fill()
right_bottom_triangle.forward(78)
right_bottom_triangle.left(108)
right_bottom_triangle.forward(45)
right_bottom_triangle.left(105)
right_bottom_triangle.forward(78)
right_bottom_triangle.end_fill()
right_bottom_triangle.hideturtle()

name = te.Turtle()
# name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()