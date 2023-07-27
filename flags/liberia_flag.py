import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Liberia"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

RED_COLOR = "#C0032C"
BLUE_COLOR = "#002468"

# The width:height ratio is 19:10
flag_width = 1280
flag_height = 673.68

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

left_bottom_x = -(flag_width / 2)
left_bottom_y = -(flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

stripe_height = 0.0909 * flag_height

stripe = te.Turtle()
# stripe.speed("fastest")
start_pos_x, start_pos_y = left_top_x, left_top_y

for stripes in range(0, 6):
    stripe.penup()
    stripe.setpos(start_pos_x, start_pos_y)
    stripe.seth(0)
    stripe.pendown()
    stripe.color("", RED_COLOR)
    stripe.begin_fill()
    stripe.forward(flag_width)
    stripe.right(90)
    stripe.forward(stripe_height)
    stripe.right(90)
    stripe.forward(flag_width)
    stripe.right(90)
    stripe.forward(stripe_height)
    stripe.end_fill()
    start_pos_y = start_pos_y - (2 * stripe_height)
stripe.hideturtle()

canton_size = 0.4545 * flag_height

canton = te.Turtle()
# canton.speed("fastest")
canton.penup()
canton.setpos(left_top_x, left_top_y)
canton.color("", BLUE_COLOR)
canton.pendown()
canton.begin_fill()
canton.forward(canton_size)
canton.right(90)
canton.forward(canton_size)
canton.right(90)
canton.forward(canton_size)
canton.right(90)
canton.forward(canton_size)
canton.end_fill()
canton.hideturtle()

star_radius = 0.07177 * flag_width
star_pos_x = left_top_x + (canton_size / 2)
star_pos_y = left_top_y - (canton_size / 2)

star = te.Turtle()
draw_five_pointed_star(star, 5, star_radius, star_pos_x, star_pos_y, "#FFFFFF", pen_color="", speed="slow")

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

def test_star_size():
    circle = te.Turtle()
    circle.penup()
    circle.setpos(star_pos_x, star_pos_y)
    circle.pendown()
    circle.speed("fast")
    circle.seth(270)
    circle.forward(star_radius)
    circle.seth(0)
    circle.circle(star_radius)

def test_star_center():
    check_center = te.Turtle()
    check_center.penup()
    check_center.setpos(left_top_x, left_top_y)
    check_center.pendown()
    check_center.speed("fast")
    check_center.forward(canton_size / 2)
    check_center.right(90)
    check_center.forward(canton_size / 2)
    check_center.right(90)
    check_center.forward(canton_size / 2)

# test_star_size()
# test_star_center()

te.done()