import turtle as te

FLAG_NAME = "Flag Of Nigeria"

GREEN_COLOR = "#008753"
WHITE_COLOR = "#FFFFFF"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 2:1
flag_width = 1200
flag_height = 600

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_width = flag_width / 3

def draw_vertical_band(tobj: te.Turtle, height, width, pos_x, pos_y, color):
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
    return pos_x + band_width, pos_y


flag = te.Turtle()
x_pos, y_pos = draw_vertical_band(flag, flag_height, band_width, left_top_x, left_top_y, GREEN_COLOR)
x_pos, y_pos = draw_vertical_band(flag, flag_height, band_width, x_pos + band_width, y_pos, GREEN_COLOR)

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()