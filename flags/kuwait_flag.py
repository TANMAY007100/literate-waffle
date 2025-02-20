import turtle as te
import math

FLAG_NAME = "Flag Of Kuwait"

DEFAULT_FIELD_COLOR = "#EAECF0"
RED_COLOR = "#CE1126"
GREEN_COLOR = "#00965E"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"

# Initialize screen
screen = te.Screen()
screen.bgcolor(DEFAULT_FIELD_COLOR)
te.title(FLAG_NAME)

# The width:height ratio is 2:1
flag_width = 1280
flag_height = 640

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = te.getcanvas().winfo_screenheight()
screen_width = te.getcanvas().winfo_screenwidth()

# Bring Window to front
# rootwindow = screen.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

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
    return pos_x, pos_y



flag = te.Turtle()
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y, GREEN_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos - band_height, WHITE_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos - band_height, RED_COLOR)

triangle_adjacent = 0.25 * flag_width

trapezoid_side = math.sqrt((band_height * band_height) + (triangle_adjacent * triangle_adjacent))
# Calculate Angles between Hypothenuse and legs of Triangle
angle_opposite_adjacent = math.atan(band_height / triangle_adjacent) * (180 / math.pi)

trapezoid = te.Turtle()
trapezoid.penup()
trapezoid.setpos(left_top_x, left_top_y)
trapezoid.pendown()
trapezoid.color("", BLACK_COLOR)
trapezoid.begin_fill()
trapezoid.right(angle_opposite_adjacent)
trapezoid.forward(trapezoid_side)
trapezoid.seth(270)
trapezoid.forward(band_height)
trapezoid.right(90 - angle_opposite_adjacent)
trapezoid.forward(trapezoid_side)
trapezoid.seth(90)
trapezoid.forward(flag_height)
trapezoid.end_fill()
trapezoid.hideturtle()

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()