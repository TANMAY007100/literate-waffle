import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Honduras"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

BLUE_COLOR = "#00BCE4"
WHITE_COLOR = "#FFFFFF"

# The width:height ratio is 2:1
flag_width = 1280
flag_height = 640

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

star_diameter = 0.0555 * flag_width
star_radius = star_diameter / 2

band_height = flag_height / 3

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
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y, BLUE_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos - band_height, BLUE_COLOR)

star = te.Turtle()
# Draw center star
draw_five_pointed_star(star, 5, star_radius, 0, 0, BLUE_COLOR)

# Minimal distance from top blue band to center of star
band_to_star_center_distance_y = 0.0833 * flag_height
band_to_star_center_distance_x = 0.3611 * flag_width

# Draw left top star
left_top_star_center_x = left_top_x + band_to_star_center_distance_x
left_top_star_center_y = left_top_y - band_height - band_to_star_center_distance_y
draw_five_pointed_star(star, 5, star_radius, left_top_star_center_x, left_top_star_center_y, BLUE_COLOR)

# Draw left bottom star
left_bottom_star_center_x = left_top_x + band_to_star_center_distance_x
left_bottom_star_center_y = left_top_y - band_height - (3 * band_to_star_center_distance_y)
draw_five_pointed_star(star, 5, star_radius, left_bottom_star_center_x, left_bottom_star_center_y, BLUE_COLOR)

# Draw right top star
right_top_star_center_x = right_top_x - band_to_star_center_distance_x
right_top_star_center_y = right_top_y - band_height - band_to_star_center_distance_y
draw_five_pointed_star(star, 5, star_radius, right_top_star_center_x, right_top_star_center_y, BLUE_COLOR)

# Draw right bottom star
right_top_star_center_x = right_top_x - band_to_star_center_distance_x
right_top_star_center_y = right_top_y - band_height - (3 * band_to_star_center_distance_y)
draw_five_pointed_star(star, 5, star_radius, right_top_star_center_x, right_top_star_center_y, BLUE_COLOR)


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
    circle.seth(270)
    circle.forward(star_radius)
    circle.seth(0)
    circle.circle(star_radius)
    circle.setpos(0, 0)
    circle.hideturtle()

def test_star_center():
    star_center = te.Turtle()
    star_center.penup()
    star_center.setpos(left_top_x, 0)
    star_center.pendown()
    star_center.forward(flag_width)
    star_center.penup()
    star_center.setpos(0, left_top_y)
    star_center.seth(270)
    star_center.pendown()
    star_center.forward(flag_height)
    star_center.hideturtle()

# Uncomment to measure the star size
# test_star_size()
# test_star_center()

# Main Loop
te.done()
