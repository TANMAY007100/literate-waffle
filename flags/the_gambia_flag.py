import turtle as te

FLAG_NAME = "Flag Of The Gambia"

RED_COLOR = "#CE1126"
BLUE_COLOR = "#0C1C8C"
GREEN_COLOR = "#3A7728"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 3:2
flag_width = 1024
flag_height = 682.67

red_green_band_height = 0.3333 * flag_height
blue_band_height = 0.2222 * flag_height
distance_between_two = 0.0555 * flag_height

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

left_bottom_x = -(flag_width / 2)
left_bottom_y = -(flag_height / 2)

screen_height = te.getcanvas().winfo_screenheight()
screen_width = te.getcanvas().winfo_screenwidth()

# Bring Window to front
# rootwindow = screen.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, int(((screen_width / 2) - (canvas_width / 2))),
             int((screen_height / 2) - (canvas_height / 2)))

red_band = te.Turtle()
# red_band.speed("fastest")
red_band.penup()
red_band.color(RED_COLOR)
red_band.setposition(left_top_x, left_top_y)
red_band.pendown()
red_band.begin_fill()
red_band.forward(flag_width)
red_band.right(90)
red_band.forward(red_green_band_height)
red_band.right(90)
red_band.forward(flag_width)
red_band.right(90)
red_band.forward(red_green_band_height)
red_band.end_fill()
red_band.hideturtle()

green_band = te.Turtle()
# green_band.speed("fastest")
green_band.penup()
green_band.setposition(left_bottom_x, left_bottom_y)
green_band.pendown()
green_band.color(GREEN_COLOR)
green_band.begin_fill()
green_band.forward(flag_width)
green_band.left(90)
green_band.forward(red_green_band_height)
green_band.left(90)
green_band.forward(flag_width)
green_band.left(90)
green_band.forward(red_green_band_height)
green_band.end_fill()
green_band.hideturtle()

blue_band = te.Turtle()
# blue_band.speed("fastest")
blue_band.penup()
blue_band.setposition(left_top_x, left_top_y - (red_green_band_height + distance_between_two))
blue_band.pendown()
blue_band.color(BLUE_COLOR)
blue_band.begin_fill()
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(blue_band_height)
blue_band.right(90)
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(blue_band_height)
blue_band.end_fill()
blue_band.hideturtle()

name = te.Turtle()
# name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()