import turtle as te

FLAG_NAME = "Flag Of Benin"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

GREEN_COLOR = "#008850"
YELLOW_COLOR = "#FCD20F"
RED_COLOR = "#E90929"

# The width:height ratio is 3:2
flag_width = 1280
flag_height = 673.68

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

right_top_x  = flag_width / 2
right_top_y  = flag_height / 2

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_height = 0.5 * flag_height
horizontal_length = flag_width - band_height

# Flag Field
green_band = te.Turtle()
green_band.penup()
green_band.setpos(left_top_x, left_top_y)
green_band.pendown()
green_band.color("", GREEN_COLOR)
green_band.begin_fill()
green_band.forward(band_height)
green_band.right(90)
green_band.forward(flag_height)
green_band.right(90)
green_band.forward(band_height)
green_band.right(90)
green_band.forward(flag_height)
green_band.end_fill()
green_band.hideturtle()

flag_band = te.Turtle()
flag_band.penup()
flag_band.setpos(right_top_x, right_top_y)
flag_band.seth(180)
flag_band.pendown()
flag_band.color("", YELLOW_COLOR)
flag_band.begin_fill()
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.left(90)
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.end_fill()

flag_band.penup()
flag_band.setpos(right_top_x, 0)
flag_band.seth(180)
flag_band.pendown()
flag_band.color("", RED_COLOR)
flag_band.begin_fill()
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.left(90)
flag_band.forward(horizontal_length)
flag_band.left(90)
flag_band.forward(band_height)
flag_band.end_fill()
flag_band.hideturtle()

name = te.Turtle()
name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()