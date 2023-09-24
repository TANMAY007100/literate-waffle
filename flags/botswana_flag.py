import turtle as te

FLAG_NAME = "Flag Of Botswana"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

BLUE_COLOR = "#6DA9D2"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"

# The width:height ratio is 3:2
flag_width = 1280
flag_height = 853.33

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

left_bottom_y = -(flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

band_height = 0.375 * flag_height

blue_band = te.Turtle()
blue_band.color("", BLUE_COLOR)
blue_band.penup()
blue_band.setpos(left_top_x, left_top_y)
blue_band.pendown()
blue_band.begin_fill()
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(band_height)
blue_band.right(90)
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(band_height)
blue_band.right(90)
blue_band.end_fill()

blue_band.penup()
blue_band.setpos(left_top_x, left_bottom_y)
blue_band.pendown()
blue_band.begin_fill()
blue_band.forward(flag_width)
blue_band.left(90)
blue_band.forward(band_height)
blue_band.left(90)
blue_band.forward(flag_width)
blue_band.left(90)
blue_band.forward(band_height)
blue_band.end_fill()
blue_band.hideturtle()

WHITE_SPACE = 0.0417 * flag_height
left_y_start = left_top_y - band_height - WHITE_SPACE
BLACK_BAND_HEIGHT = 0.1667 * flag_height

black_band = te.Turtle()
black_band.color("", BLACK_COLOR)
black_band.penup()
black_band.setpos(left_top_x, left_y_start)
black_band.pendown()
black_band.begin_fill()
black_band.forward(flag_width)
black_band.right(90)
black_band.forward(BLACK_BAND_HEIGHT)
black_band.right(90)
black_band.forward(flag_width)
black_band.right(90)
black_band.forward(BLACK_BAND_HEIGHT)
black_band.end_fill()
black_band.hideturtle()

name = te.Turtle()
# name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()