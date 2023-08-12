import turtle as te

FLAG_NAME = "Flag Of Switzerland"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

RED_COLOR = "#FF0000"
WHITE_COLOR = "#FFFFFF"

# The width:height ratio is 1:1
flag_width = 1024
flag_height = 1024

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

red_field = te.Turtle()
red_field.penup()
red_field.setpos(left_top_x, left_top_y)
red_field.color("", RED_COLOR)
red_field.pendown()
red_field.begin_fill()
for _ in range(0, 4):
    red_field.forward(flag_width)
    red_field.right(90)
red_field.end_fill()
red_field.hideturtle()

x_distance = left_top_x + (0.4063 * flag_width)
y_distance = left_top_y - (0.1875 * flag_height)
cross_width = 0.1875 * flag_height
cross_height = 0.2188 * flag_width

white_cross = te.Turtle()
white_cross.penup()
white_cross.setpos(x_distance, y_distance)
white_cross.color("", WHITE_COLOR)
white_cross.pendown()
white_cross.begin_fill()

for _ in range(0, 4):
    white_cross.forward(cross_width)
    white_cross.right(90)
    white_cross.forward(cross_height)
    white_cross.left(90)
    white_cross.forward(cross_height)
    white_cross.right(90)

white_cross.end_fill()
white_cross.hideturtle()

te.done()