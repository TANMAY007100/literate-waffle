import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Vietnam"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

FIELD_COLOR = "#DA251D"
STAR_COLOR = "#FFFF00"

# The width:height ratio is 3:2
flag_width = 1200
flag_height = 800

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

star_diameter = 0.4 * flag_width
star_radius = star_diameter / 2

flag_field = te.Turtle()
# flag_field.speed("fast")
flag_field.penup()
flag_field.setpos(left_top_x, left_top_y)
flag_field.pendown()
flag_field.color("", FIELD_COLOR)
flag_field.begin_fill()
flag_field.forward(flag_width)
flag_field.right(90)
flag_field.forward(flag_height)
flag_field.right(90)
flag_field.forward(flag_width)
flag_field.right(90)
flag_field.forward(flag_height)
flag_field.end_fill()
flag_field.hideturtle()

star = te.Turtle()
draw_five_pointed_star(star, 5, star_radius, 0, 0, STAR_COLOR)

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

# Uncomment to measure the star size
# test_star_size()

# Main Loop
te.done()
