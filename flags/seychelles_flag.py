import turtle as te
import math

# Initialize screen
screen = te.Screen()
te.title("Flag Of Seychelles")

# The width:height ratio is 2:1
flag_width = 1280
flag_height = 640

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

left_bottom_x = -(flag_width / 2)
left_bottom_y = -(flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

blue_area = 0.3333 * flag_width
yellow_area = 0.6667 * flag_width
top_red_area = flag_width
right_red_area = 0.3333 * flag_height
green_area = 0.3333 * flag_height

blue_diagonal = math.sqrt(flag_height * flag_height + blue_area * blue_area)
blue_hypo_adjacent = math.atan(flag_height / blue_area) * (180 / math.pi)

yellow_diagonal = math.sqrt(flag_height * flag_height + yellow_area * yellow_area)
yellow_hypo_adjacent = math.atan(flag_height / yellow_area) * (180 / math.pi)

red_diagonal = math.sqrt(flag_height * flag_height + right_red_area * right_red_area)
red_hypo_adjacent = math.atan(flag_height / right_red_area) * (180 / math.pi)

green_diagonal = math.sqrt(flag_width * flag_width + green_area * green_area)
green_hypo_adjacent = math.atan(green_area / flag_width) * (180 / math.pi)

# Blue Band
flag_turtle = te.Turtle()
flag_turtle.penup()
# flag_turtle.speed("fast")
flag_turtle.setpos(left_bottom_x, left_bottom_y)
flag_turtle.pendown()
flag_turtle.color("", "#003D88")
flag_turtle.begin_fill()
flag_turtle.left(blue_hypo_adjacent)
flag_turtle.forward(blue_diagonal)
flag_turtle.seth(180)
flag_turtle.forward(blue_area)
flag_turtle.left(90)
flag_turtle.forward(flag_height)
flag_turtle.end_fill()

# Yellow Band
flag_turtle.penup()
# flag_turtle.speed("fast")
flag_turtle.setpos(left_bottom_x, left_bottom_y)
flag_turtle.seth(0)
flag_turtle.pendown()
flag_turtle.color("", "#FCD955")
flag_turtle.begin_fill()
flag_turtle.left(yellow_hypo_adjacent)
flag_turtle.forward(yellow_diagonal)
flag_turtle.seth(180)
flag_turtle.forward(yellow_area - blue_area)
flag_turtle.left(blue_hypo_adjacent)
flag_turtle.forward(blue_diagonal)
flag_turtle.end_fill()

# Red Band
flag_turtle.penup()
# flag_turtle.speed("fast")
flag_turtle.setpos(left_bottom_x, left_bottom_y)
flag_turtle.seth(0)
flag_turtle.pendown()
flag_turtle.color("", "#D92323")
flag_turtle.begin_fill()
flag_turtle.left(yellow_hypo_adjacent)
flag_turtle.forward(yellow_diagonal)
flag_turtle.seth(0)
flag_turtle.forward(top_red_area - yellow_area)
flag_turtle.seth(270)
flag_turtle.forward(right_red_area)
flag_turtle.right(red_hypo_adjacent)
flag_turtle.forward(red_diagonal)
flag_turtle.end_fill()

# Green Band
flag_turtle.penup()
# flag_turtle.speed("fast")
flag_turtle.setpos(left_bottom_x, left_bottom_y)
flag_turtle.seth(0)
flag_turtle.pendown()
flag_turtle.color("", "#007A3A")
flag_turtle.begin_fill()
flag_turtle.left(green_hypo_adjacent)
flag_turtle.forward(green_diagonal)
flag_turtle.seth(270)
flag_turtle.forward(green_area)
flag_turtle.right(90)
flag_turtle.forward(flag_width)
flag_turtle.end_fill()

flag_turtle.hideturtle()

te.done()