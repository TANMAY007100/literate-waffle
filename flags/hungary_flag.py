import turtle as te

# Initialize screen
screen = te.Screen()
te.title("Flag Of Hungary")

# The width:height ratio is 2:1
flag_width = 1280
flag_height = 640

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

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
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y, "#CE2939")
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos - (2 * band_height), "#477050")

te.done()