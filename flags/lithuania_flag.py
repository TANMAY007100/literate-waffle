import turtle as te

FLAG_NAME = "Flag Of Lithuania"

YELLOW_COLOR = "#FDB913"
GREEN_COLOR = "#006A44"
RED_COLOR = "#C1272D"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 5:3
flag_width = 800
flag_height = 480

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = te.getcanvas().winfo_screenheight()
screen_width = te.getcanvas().winfo_screenwidth()

# Bring Window to front
# rootwindow = screen.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, int((screen_width / 2) - (canvas_width / 2)),
             int((screen_height / 2) - (canvas_height / 2)))

band_height = (1 / 3) * flag_height

def make_band(tobj: te.Turtle, colour: str, pos_x: float, pos_y: float, length: float, height: float):
    tobj.showturtle()
    tobj.color("", colour)
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
    return (pos_x, pos_y-band_height)


band_turtle = te.Turtle()
# band_turtle.speed("fastest")
next_pos_x, next_pos_y = make_band(band_turtle, YELLOW_COLOR, left_top_x, left_top_y, flag_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, GREEN_COLOR, next_pos_x, next_pos_y, flag_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, RED_COLOR, next_pos_x, next_pos_y, flag_width, band_height)

name = te.Turtle()
# name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()