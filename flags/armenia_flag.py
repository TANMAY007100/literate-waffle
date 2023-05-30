import turtle as te

# Initialize screen
screen = te.Screen()
te.title("Flag Of Armenia")

# The width:height ratio is 2:1
flag_width = 900
flag_height = 450

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# Setting width and height of window dynamically
screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_height = (1 / 3) * flag_height

def make_band(tobj: te.Turtle, colour: str, pos_x: float, pos_y: float, length: float, height: float):
    tobj.showturtle()
    tobj.color(colour, colour)
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
# band_turtle.speed("normal")
next_pos_x, next_pos_y = make_band(band_turtle, "#D90012", left_top_x, left_top_y, flag_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, "#0033A0", next_pos_x, next_pos_y, flag_width, band_height)
next_pos_x, next_pos_y = make_band(band_turtle, "#F2A800", next_pos_x, next_pos_y, flag_width, band_height)

te.done()