import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Chile"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

BLUE_COLOR = "#0039A6"
WHITE_COLOR = "#FFFFFF"
RED_COLOR = "#D52B1E"

# The width:height ratio is 3:2
flag_width = 1280
flag_height = 853.33

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

right_top_x = flag_width / 2
right_top_y = flag_height / 2

left_bottom_x = -(flag_width / 2)
left_bottom_y = -(flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

star_diameter = 0.1666 * flag_width
star_radius = star_diameter / 2

band_height = flag_height / 2

def draw_band(tobj: te.Turtle, height, width, pos_x, pos_y, color):
    tobj.showturtle()
    tobj.penup()
    tobj.setpos(pos_x, pos_y)
    tobj.seth(0)
    tobj.pendown()
    tobj.color("", color)
    tobj.begin_fill()
    tobj.forward(width)
    tobj.right(90)
    tobj.forward(height)
    tobj.right(90)
    tobj.forward(width)
    tobj.right(90)
    tobj.forward(height)
    tobj.end_fill()
    tobj.hideturtle()
    return pos_x, pos_y - band_height


flag = te.Turtle()
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y - band_height, RED_COLOR)
x_pos, y_pos = draw_band(flag, band_height, band_height, left_top_x, left_top_y, BLUE_COLOR)

star = te.Turtle()
# Distance from left
x_distance = 0.1666 * flag_width
# Distance from top
y_distance = 0.25 * flag_height
draw_five_pointed_star(star, 5, star_radius, left_top_x + x_distance, left_top_y - y_distance, WHITE_COLOR)

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

def test_star_size():
    circle = te.Turtle()
    circle.speed("fast")
    circle.penup()
    circle.setpos(left_top_x + x_distance, left_top_y - y_distance)
    circle.pendown()
    circle.forward(star_radius)
    circle.seth(270)
    circle.circle(-star_radius)
    circle.hideturtle()

def test_star_center():
    star_center = te.Turtle()
    star_center.speed("fast")
    star_center.penup()
    star_center.setpos(left_top_x, left_top_y)
    star_center.pendown()
    star_center.forward(x_distance)
    star_center.right(90)
    star_center.forward(y_distance)
    star_center.right(90)
    star_center.forward(x_distance)
    star_center.right(90)
    star_center.forward(y_distance)
    star_center.hideturtle()

# Uncomment to measure the star size
# test_star_size()
# test_star_center()

# Main Loop
te.done()
