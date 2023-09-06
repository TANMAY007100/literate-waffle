import turtle as te
import math
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Central African Republic"

BLUE_COLOR = "#003082"
GREEN_COLOR = "#289728"
YELLOW_COLOR = "#FFCE00"
WHITE_COLOR = "#FFFFFF"
RED_COLOR = "#D21034"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 3:2
flag_width = 1280
flag_height = 853.33

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_height = flag_height / 4

# Original Formula
# A = (107 - 9 * math.sqrt(5)) / 16
A = 0.1357 * flag_height
# Original Formula
# B = (35 - 9 * math.sqrt(5)) / 16
B = 0.0232 * flag_height


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
    return pos_x, pos_y


flag = te.Turtle()
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y, BLUE_COLOR)
# x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, y_pos - band_height, WHITE_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, y_pos - (2 * band_height), GREEN_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, y_pos - band_height, YELLOW_COLOR)
x_pos, y_pos = draw_band(flag, flag_height, band_height, 0 - (band_height / 2), left_top_y, RED_COLOR)

circle_diameter = 0.225 * flag_height
star_radius = circle_diameter / 2
star_pos_x = left_top_x + band_height
star_pos_y = left_top_y - A

star = te.Turtle()
draw_five_pointed_star(star, 5, star_radius, star_pos_x, star_pos_y, YELLOW_COLOR, pen_color="", speed="slow")

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

def test_star():
    star_distance = te.Turtle()
    star_distance.setpos(left_top_x, (left_top_y - band_height) + B)

te.done()