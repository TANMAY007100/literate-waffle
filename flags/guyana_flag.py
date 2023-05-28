import math
import turtle as te

# Initialize screen
screen = te.Screen()
te.title("Flag Of Guyana")

# The width:height ratio is 5:3
flag_width = 800
flag_height = 480

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

# Setting width and height of window dynamically
screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

green_forests = te.Turtle()
green_forests.penup()
green_forests.setpos(left_top_x, left_top_y)
green_forests.color("#FFFFFF", "#25946A")
green_forests.begin_fill()
green_forests.forward(flag_width)
green_forests.right(90)
green_forests.forward(flag_height)
green_forests.right(90)
green_forests.forward(flag_width)
green_forests.right(90)
green_forests.forward(flag_height)
green_forests.end_fill()
green_forests.hideturtle()

# Calculation reference = https://www.omnicalculator.com/math/right-triangle-side-angle

# Angle between Hypothenus and Adjacent side
# This angle is not needed. However, it is kept for reference.
# hypo_adjacent = math.atan(((flag_height / 2) / flag_width)) * (180 / math.pi)
# Angle between Hypothenus and Opposite side
hypo_opposite = math.atan(flag_width / (flag_height / 2)) * (180 / math.pi)
# Calculate Hypothenus of Half Triangle
# Hypotenuse = Square Root of (Square of Width of Flag plus Square of Half of Height of Flag)
# Note: In this case the width is common and therefore calcualtion is based on half of height.
half_hypotenuse = math.sqrt(((flag_height / 2) * (flag_height / 2)) + (flag_width * flag_width))

# White Water
white_water = te.Turtle()
white_water.penup()
white_water.setpos(left_top_x, left_top_y)
white_water.seth(270)
white_water.color("#FFFFFF")
white_water.pendown()
white_water.begin_fill()
white_water.left(hypo_opposite)
white_water.forward(half_hypotenuse)
white_water.seth(270)
white_water.right(hypo_opposite)
white_water.forward(half_hypotenuse)
white_water.seth(90)
white_water.forward(flag_height)
white_water.end_fill()
white_water.hideturtle()

# Gold Mineral
gold_mineral = te.Turtle()
gold_mineral.penup()
gold_mineral.setpos(left_top_x, left_top_y - (0.0333 * left_top_y))
gold_mineral.seth(270)
gold_mineral.color("#FFC303")
gold_mineral.pendown()
gold_mineral.begin_fill()
gold_mineral.left(hypo_opposite)
gold_mineral.forward(half_hypotenuse - (0.0333 * half_hypotenuse))
gold_mineral.seth(270)
gold_mineral.right(hypo_opposite)
gold_mineral.forward(half_hypotenuse - (0.0333 * half_hypotenuse))
gold_mineral.end_fill()
gold_mineral.hideturtle()


# Angle between Hypothenus and Opposite side
endurance_hypo_opposite = math.atan((flag_width / 2) / (flag_height / 2)) * (180 / math.pi)
endurance_hypothenus = math.sqrt((flag_height * flag_height) + (flag_width * flag_width))

# Black Endurance
black_endurance = te.Turtle()
black_endurance.penup()
black_endurance.setpos(left_top_x, left_top_y)
black_endurance.seth(270)
black_endurance.color("#000000")
black_endurance.pendown()
black_endurance.begin_fill()
black_endurance.left(endurance_hypo_opposite)
black_endurance.forward(endurance_hypothenus / 2)
black_endurance.seth(270)
black_endurance.right(endurance_hypo_opposite)
black_endurance.forward(endurance_hypothenus / 2)
black_endurance.end_fill()
black_endurance.hideturtle()

zeal_left_top_y = left_top_y - (0.05 * left_top_y)
zeal_hypothenus = (endurance_hypothenus  - (0.05 * endurance_hypothenus)) / 2

# Red Zeal & Dynamism
red_zeal = te.Turtle()
red_zeal.penup()
red_zeal.setpos(left_top_x, zeal_left_top_y)
red_zeal.seth(270)
red_zeal.color("#C01829")
red_zeal.pendown()
red_zeal.begin_fill()
red_zeal.left(endurance_hypo_opposite)
red_zeal.forward(zeal_hypothenus)
red_zeal.seth(270)
red_zeal.right(endurance_hypo_opposite)
red_zeal.forward(zeal_hypothenus)
red_zeal.end_fill()
red_zeal.hideturtle()

te.done()
