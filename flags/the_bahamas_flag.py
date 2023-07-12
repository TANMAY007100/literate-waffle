import turtle as te

FLAG_NAME = "Flag Of The Bahamas"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 2:1
flag_width = 1280
flag_height = 640

canvas_width = flag_width + 100
canvas_height = flag_height + 200

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
# flag.speed("fast")
x_pos, y_pos = draw_band(flag, band_height, flag_width, left_top_x, left_top_y, "#00778B")
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos - band_height, "#FFC72C")
x_pos, y_pos = draw_band(flag, band_height, flag_width, x_pos, y_pos - band_height, "#00778B")

# Black Triangle
triangle = te.Turtle()
# triangle.speed("fast")
triangle.penup()
triangle.setpos(left_top_x, left_top_y)
triangle.pendown()
triangle.begin_fill()
triangle.right(30)
triangle.forward(flag_height)
triangle.right(180 - 60)
triangle.forward(flag_height)
triangle.seth(90)
triangle.forward(flag_height)
triangle.end_fill()
triangle.hideturtle()

# Uncomment to measure
# measure = te.Turtle()
# measure.seth(270)
# measure.penup()
# measure.forward(flag_height / 2)
# measure.pendown()
# measure.seth(90)
# measure.forward(flag_height)
# measure.hideturtle()
# import time
# time.sleep(20)
# measure.clear()

name = te.Turtle()
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()


te.done()