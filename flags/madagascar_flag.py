import turtle as te


# Initialize screen
screen = te.Screen()
te.title("Flag Of Madagascar")

# The width:height ratio is 25:18
flag_width = 1280
flag_height = 853

canvas_width = flag_width + 100
canvas_height = flag_height + 100

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
# This is just to be able to see the flag as the left part of flag is white
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

flag_band = te.Turtle()
flag_band.penup()
flag_band.setpos(right_top_x, right_top_y)
flag_band.seth(180)
flag_band.pendown()
flag_band.color("#FC3B2E", "#FC3B2E")
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
flag_band.color("#027F36", "#027F36")
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

te.done()