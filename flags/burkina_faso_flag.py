import turtle as te
from utils import draw_five_pointed_star

FLAG_NAME = "Flag Of Burkina Faso"

RED_COLOR = "#EF2B2D"
GREEN_COLOR = "#009E49"
YELLOW_COLOR = "#FCD116"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

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

circle_diameter = 0.2222 * flag_width
circle_radius = circle_diameter / 2
band_height = 0.5 * flag_height

band = te.Turtle()
band.speed("fastest")
band.penup()
band.setpos(left_top_x, left_top_y)
band.color("", RED_COLOR)
band.pendown()
band.begin_fill()
band.forward(flag_width)
band.right(90)
band.forward(band_height)
band.right(90)
band.forward(flag_width)
band.right(90)
band.forward(band_height)
band.end_fill()

band.penup()
band.setpos(left_top_x, left_top_y - band_height)
band.seth(0)
band.color("", GREEN_COLOR)
band.pendown()
band.begin_fill()
band.forward(flag_width)
band.right(90)
band.forward(band_height)
band.right(90)
band.forward(flag_width)
band.right(90)
band.forward(band_height)
band.end_fill()
band.hideturtle()

star = te.Turtle()
draw_five_pointed_star(star, 5, circle_radius, 0, 0, YELLOW_COLOR)

name = te.Turtle()
name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

def test_star_center():
    test_star = te.Turtle()
    test_star.penup()
    test_star.setpos(left_top_x, 0)
    test_star.pendown()
    test_star.forward(flag_width)

    test_star.penup()
    test_star.setpos(0, left_top_y)
    test_star.pendown()
    test_star.seth(270)
    test_star.forward(flag_height)
    test_star.hideturtle()

# test_star_center()

te.done()
