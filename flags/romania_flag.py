import turtle as te
import math


screen_width = 2056
screen_height = 1329

# Initialize screen
screen = te.Screen()
te.title("Flag Of Romania")

# The width:height ratio is 3:2
flag_width = 900
flag_height = 600

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_width = (1 / 3) * flag_width
band_height = flag_height

def make_band(tobj: te.Turtle, colour: str, pos_x: float, pos_y: float, length: float, height: float):
    tobj.showturtle()
    tobj.color(colour)
    tobj.penup()
    tobj.setpos(pos_x, pos_y)
    tobj.pendown()
    tobj.begin_fill()
    for _ in range(0, 2):
        tobj.forward(length)
        tobj.right(90)
        tobj.forward(height)
        tobj.right(90)
    tobj.end_fill()
    tobj.hideturtle()
    return (pos_x+band_width, left_top_y)


band_turtle = te.Turtle()
next_pos_x, next_pos_y = make_band(band_turtle, "#002B7F", left_top_x, left_top_y, band_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, "#FCD116", next_pos_x, next_pos_y, band_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, "#CE1126", next_pos_x, next_pos_y, band_width, band_height)


te.done()