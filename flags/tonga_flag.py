import turtle as te


# Initialize screen
screen = te.Screen()
te.title("Flag Of Tonga")

# The width:height ratio is 2:1
flag_width = 800
flag_height = 400

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

white_canton_width = (41.6 * flag_width) / 100
white_canton_height = (50 * flag_height) / 100

# Cross side is 12.5 percent of flag height
red_cross_side = 0.125 * flag_height

red_bg = te.Turtle()
red_bg.penup()
red_bg.setpos(left_top_x, left_top_y)
red_bg.pendown()
red_bg.color("#C20000")
red_bg.begin_fill()
red_bg.forward(flag_width)
red_bg.right(90)
red_bg.forward(flag_height)
red_bg.right(90)
red_bg.forward(flag_width)
red_bg.right(90)
red_bg.forward(flag_height)
red_bg.right(90)
red_bg.end_fill()
red_bg.hideturtle()

white_canton = te.Turtle()
white_canton.penup()
white_canton.setpos(left_top_x, 0)
white_canton.pendown()
white_canton.color("#FFFFFF")
white_canton.begin_fill()
white_canton.forward(white_canton_width)
white_canton.seth(90)
white_canton.forward(white_canton_height)
white_canton.left(90)
white_canton.forward(white_canton_width)
white_canton.left(90)
white_canton.forward(white_canton_height)
white_canton.end_fill()
white_canton.hideturtle()

rc_x_pos = (white_canton_width / 2) - (red_cross_side + (red_cross_side / 2))
rc_y_pos = (white_canton_height / 2)

red_cross = te.Turtle()
red_cross.penup()
red_cross.color("#C20000")
red_cross.setpos(left_top_x, rc_y_pos)
red_cross.forward(rc_x_pos)
red_cross.pendown()
# Starting point of red cross
red_cross.begin_fill()
red_cross.seth(90)
red_cross.forward(red_cross_side / 2)
red_cross.right(90)
for _ in range(0, 4):
    red_cross.forward(red_cross_side)
    red_cross.left(90)
    red_cross.forward(red_cross_side)
    red_cross.right(90)
    red_cross.forward(red_cross_side)
    red_cross.right(90)
red_cross.end_fill()
red_cross.hideturtle()

# Uncomment to check centre of red cross inside white canton
# measure = te.Turtle()
# measure.penup()
# measure.color("#0000FF")
# measure.setpos(left_top_x, rc_y_pos)
# measure.pendown()
# measure.forward(white_canton_width / 2)
# measure.left(90)
# measure.forward(white_canton_height / 2)
# measure.hideturtle()

te.done()