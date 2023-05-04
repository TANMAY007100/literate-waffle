import turtle as te


screen_width = 2056
screen_height = 1329
flag_width = 1000
flag_height = 500

canvas_width = flag_width + 100
canvas_height = flag_height + 100

# Initialize screen
screen = te.Screen()
te.title("Flag Of Latvia")
# The width:height ratio is 2:1

# TODO Make screen_height and screen_width values taken from actual screen.
screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

band_height = (40 / 100) * flag_height

def draw_band(tobj: te.Turtle, length, height):
    tobj.begin_fill()
    tobj.forward(length)
    tobj.right(90)
    tobj.forward(height)
    tobj.right(90)
    tobj.forward(length)
    tobj.right(90)
    tobj.forward(height)
    tobj.end_fill()

flag_turtle = te.Turtle()
flag_turtle.penup()
flag_turtle.setpos(left_top_x, left_top_y)
flag_turtle.pendown()
flag_turtle.color("#9D2235")
draw_band(flag_turtle, flag_width, band_height)
flag_turtle.penup()
flag_turtle.setpos(left_top_x, -(left_top_y - band_height))
flag_turtle.right(90)
flag_turtle.pendown()
draw_band(flag_turtle, flag_width, band_height)
flag_turtle.hideturtle()

te.done()