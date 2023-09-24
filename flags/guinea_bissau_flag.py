import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Guinea-Bissau"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

GREEN_COLOR = "#009E49"
YELLOW_COLOR = "#FCD116"
RED_COLOR = "#CE1126"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"

# The width:height ratio is 2:1
flag_width = 1280
flag_height = 640

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

right_top_x  = flag_width / 2
right_top_y  = flag_height / 2

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_height = 0.5 * flag_height
horizontal_length = flag_width - band_height

red_band = te.Turtle()
red_band.penup()
red_band.setpos(left_top_x, left_top_y)
red_band.pendown()
red_band.color("", RED_COLOR)
red_band.begin_fill()
red_band.forward(band_height)
red_band.right(90)
red_band.forward(flag_height)
red_band.right(90)
red_band.forward(band_height)
red_band.right(90)
red_band.forward(flag_height)
red_band.end_fill()
red_band.hideturtle()

flag_band = te.Turtle()
flag_band.penup()
flag_band.setpos(right_top_x, right_top_y)
flag_band.seth(180)
flag_band.pendown()
flag_band.color("", YELLOW_COLOR)
flag_band.begin_fill()
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.left(90)
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.end_fill()

flag_band.penup()
flag_band.setpos(right_top_x, 0)
flag_band.seth(180)
flag_band.pendown()
flag_band.color("", GREEN_COLOR)
flag_band.begin_fill()
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.left(90)
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.end_fill()
flag_band.hideturtle()

star_diameter = (1 / 3) * flag_height
star_radius = star_diameter / 2

star_pos_x = left_top_x + (band_height / 2)
star_pos_y = 0

star = te.Turtle()
draw_five_pointed_star(star, 5, star_radius, star_pos_x, star_pos_y, BLACK_COLOR, pen_color="", speed="slow")

name = te.Turtle()
name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

def test_star_center():
    red_center = te.Turtle()
    # red_center.speed("fastest")
    red_center.color(WHITE_COLOR)
    red_center.penup()
    red_center.setpos(left_top_x, left_top_y)
    red_center.forward(band_height / 2)
    red_center.pendown()
    red_center.right(90)
    red_center.forward(flag_height)
    red_center.penup()
    red_center.setpos(left_top_x, 0)
    red_center.seth(0)
    red_center.pendown()
    red_center.forward(flag_width)
    red_center.hideturtle()

# test_star_center()

te.done()