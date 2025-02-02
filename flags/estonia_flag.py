import turtle as te

FLAG_NAME = "Flag Of Estonia"

DEFAULT_FIELD_COLOR = "#EAECF0"
BLUE_COLOR = "#0072CE"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"

# Initialize screen
screen = te.Screen()
# Set the background color
screen.bgcolor(DEFAULT_FIELD_COLOR)
te.title(FLAG_NAME)

# The width:height ratio is 11:7
flag_width = 1024
flag_height = 651.64

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = te.getcanvas().winfo_screenheight()
screen_width = te.getcanvas().winfo_screenwidth()

# Bring Window to front
# rootwindow = screen.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, int((screen_width / 2) - (canvas_width / 2)), int((screen_height / 2) - (canvas_height / 2)))

band_height = flag_height / 3

def draw_band(tobj: te.Turtle, height, width, pos_x, pos_y, color):
    tobj.showturtle()
    tobj.penup()
    tobj.setpos(pos_x, pos_y)
    tobj.seth(0)
    tobj.pendown()
    tobj.color(color, color)
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
    return pos_x, pos_y - band_height

flag = te.Turtle()
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y, BLUE_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos, BLACK_COLOR)
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos, WHITE_COLOR)

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()