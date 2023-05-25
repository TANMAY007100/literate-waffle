import turtle as te
import math

# Initialize screen
screen = te.Screen()
te.title("Flag Of Jordan")

# The width:height ratio is 2:1
flag_width = 840
flag_height = 420

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# Setting width and height of window dynamically
screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

angle_1 = (math.atan(2) * (180 / 3.1417)) / 2
angle_2 = (math.atan(2) / 2) * (180 / 3.1417)

band_height = flag_height / 3

def draw_band(tobj, px, py, color, x_dist, y_dist):
    tobj.penup()
    tobj.setpos(px, py)
    tobj.color(color)
    tobj.pendown()
    tobj.begin_fill()
    tobj.forward(x_dist)
    tobj.right(90)
    tobj.forward(y_dist)
    tobj.right(90)
    tobj.forward(x_dist)
    tobj.right(90)
    tobj.forward(y_dist)
    tobj.end_fill()
    tobj.right(90)
    return px, py - y_dist

# Flag bands
band = te.Turtle()
pos_x, pos_y = draw_band(band, left_top_x, left_top_y, "#000000", flag_width, band_height)
pos_x, pos_y = draw_band(band, pos_x, pos_y, "#FFFFFF", flag_width, band_height)
pos_x, pos_y = draw_band(band, pos_x, pos_y, "#007a3d", flag_width, band_height)
band.hideturtle()


red_chevron = te.Turtle()
red_chevron.penup()
red_chevron.setpos(left_top_x, -left_top_y)
red_chevron.seth(90)
red_chevron.color("#CE1126")
red_chevron.pendown()
red_chevron.begin_fill()
red_chevron.right(angle_1)
red_chevron.right(angle_2)
# Calculating the diagonal
# Diagonal = The Diagonal is calculated by squaring both height and width, suming them up and then taking their square root.
# Diagonal = Square root of (Square of Width plus Square of Height)
d = math.sqrt((flag_height * flag_height) + (flag_width * flag_width))
red_chevron.forward(d / 2)
red_chevron.seth(90)
red_chevron.left(angle_1)
red_chevron.left(angle_2)
red_chevron.forward(d / 2)
red_chevron.end_fill()
red_chevron.hideturtle()

# A = ((math.sqrt(5) * 21) - 21) / 2
# A = 12.978713763747791
# A is aprrox 15.45 percent of flag width

A = 0.1545 * flag_width

star = te.Turtle()
angle = 360 / 7
side = 0.03571 * flag_height
side_angle = angle * 1.8
star.penup()
star.setpos(-311, -7)
star.pendown()
star.color("#FFFFFF")
star.begin_fill()
for i in range(7): 
    star.forward(side)
    star.right(side_angle)
    star.forward(side)
    star.left(144)
star.end_fill()
star.hideturtle()


# Uncomment to find the centre for the star
# measure = te.Turtle()
# measure.setpos(left_top_x, -left_top_y)
# measure.seth(90)
# measure.color("#00FF00")
# measure.pendown()
# measure.right(angle_1)
# measure.forward(d / 2)
# measure.penup()
# measure.setpos(left_top_x, left_top_y)
# measure.seth(270)
# measure.color("#00FF00")
# measure.pendown()
# measure.left(angle_1)
# measure.forward(d / 2)
# measure.penup()
# measure.setpos(0, 0)
# measure.seth(180)
# measure.color("#0000FF")
# measure.pendown()
# measure.forward(flag_width / 2)
# measure.hideturtle()

te.done()