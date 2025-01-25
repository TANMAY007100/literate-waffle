import turtle as te

from utils import draw_nauru_star

FLAG_NAME = "Flag Of Nauru"

BLUE_COLOR = "#012169"
YELLOW_COLOR = "#FFC72C"
WHITE_COLOR = "#FFFFFF"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 2:1
flag_width = 1024
flag_height = 512

band_height = 0.5 * flag_height
band_width = flag_width

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

left_bottom_x = -(flag_width / 2)
left_bottom_y = -flag_height

screen_height = te.getcanvas().winfo_screenheight()
screen_width = te.getcanvas().winfo_screenwidth()

# Bring Window to front
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, int((screen_width / 2) - (canvas_width / 2)), int((screen_height / 2) - (canvas_height / 2)))

blue_band = te.Turtle()
blue_band.penup()
# blue_band.speed("fastest")
blue_band.setpos(left_top_x, left_top_y)
blue_band.pendown()
blue_band.color(BLUE_COLOR, BLUE_COLOR)
blue_band.begin_fill()
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(flag_height)
blue_band.right(90)
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(flag_height)
blue_band.right(90)
blue_band.end_fill()
blue_band.hideturtle()

yellow_band_height = 0.08333 * flag_height
yellow_band_top_edge_y  = left_top_y - (0.45833 * flag_height)
yellow_band_bottom_edge_y  = left_bottom_y + (0.45833 * flag_height)

yellow_band = te.Turtle()
yellow_band.penup()
# yellow_band.speed("fastest")
yellow_band.setpos(left_top_x, yellow_band_top_edge_y)
yellow_band.seth(0)
yellow_band.pendown()
yellow_band.color(YELLOW_COLOR, YELLOW_COLOR)
yellow_band.begin_fill()
yellow_band.forward(flag_width)
yellow_band.right(90)
yellow_band.forward(yellow_band_height)
yellow_band.right(90)
yellow_band.forward(flag_width)
yellow_band.right(90)
yellow_band.forward(yellow_band_height)
yellow_band.right(90)
yellow_band.end_fill()
yellow_band.hideturtle()

# Calculations
x = left_top_x + (0.25 * flag_width)
y = left_top_y - (0.7083 * flag_height)
radius = (0.0833 * flag_width) / 2

# Draw triangles
triangles = te.Turtle()
draw_nauru_star(triangles, x, y, radius)

# Draw inner circle
inner_circle = te.Turtle()
# inner_circle.speed("fastest")
inner_circle.color(WHITE_COLOR)
inner_circle.penup()
inner_circle.setposition(x, y)
inner_circle.backward(radius)
inner_circle.pendown()
inner_circle.setheading(270)
inner_circle.begin_fill()
inner_circle.circle(radius)
inner_circle.end_fill()
inner_circle.hideturtle()

def test_outer_circle():
    test_outer_circle = (0.1667 * flag_width) / 2
    outer_circle = te.Turtle()
    outer_circle.color("#FF0000", "")
    outer_circle.speed("fastest")
    outer_circle.penup()
    outer_circle.setposition(x, y)
    outer_circle.backward(test_outer_circle)
    outer_circle.pendown()
    outer_circle.setheading(270)
    outer_circle.circle(test_outer_circle)
    outer_circle.hideturtle()

# test_outer_circle()

name = te.Turtle()
# name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()