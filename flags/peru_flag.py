import turtle as te

FLAG_NAME = "Flag Of Peru"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 3:2
flag_width = 900
flag_height = 600

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# Setting width and height of window dynamically
screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_width = (1 / 3) * flag_width
band_height = flag_height

RED_COLOR = "#D91023"

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
    return (pos_x, left_top_y)

# Flag Field
# This is just to be able to see the flag as the center part of flag is white
# Note: There is no black border around the flag.
flag_field = te.Turtle()
flag_field.penup()
flag_field.setpos(left_top_x, left_top_y)
flag_field.speed("fastest")
flag_field.seth(0)
flag_field.pendown()
flag_field.color("#000000", "#FFFFFF")
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


band_turtle = te.Turtle()
# band_turtle.speed("fast")
next_pos_x, next_pos_y = make_band(band_turtle, RED_COLOR, left_top_x, left_top_y, band_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, RED_COLOR, next_pos_x + (2 * band_width), next_pos_y, band_width, band_height)

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()