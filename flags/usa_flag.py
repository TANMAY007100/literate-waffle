import turtle as te
import math

# Initialize screen
screen = te.Screen()
# The width:height ratio is 10:19
width = 1710
hoist_height = 900
# Alternate Colors
color_stripe = ["#B22234", "#FFFFFF"]
stripe_color = 0
# Hoist of the canton
hoist_of_the_canton = math.ceil(hoist_height * (7/13))
fly_of_the_canton = math.floor(width * (2/5))
screen.setup(width, hoist_height)
next_stripe_position = 450
stripe_width = math.ceil((1 / 13) * hoist_height)
first_stripe_turtle = te.Turtle()
first_stripe_turtle.speed("fastest")
start_position = -855
first_stripe_turtle.penup()
first_stripe_turtle.setpos((start_position, next_stripe_position))
first_stripe_turtle.pendown()
first_stripe_turtle.color(color_stripe[stripe_color])
first_stripe_turtle.begin_fill()
first_stripe_turtle.forward(width)
first_stripe_turtle.right(90)
first_stripe_turtle.forward(stripe_width)
first_stripe_turtle.right(90)
first_stripe_turtle.forward(width)
first_stripe_turtle.end_fill()
first_stripe_turtle.hideturtle()
start_strip_location = 0
for alternate_strips in range(0, 13):
    stripe_turtle = te.Turtle()
    stripe_turtle.speed("fastest")
    stripe_turtle.color(color_stripe[stripe_color])
    stripe_turtle.penup()
    stripe_turtle.setpos((start_position, next_stripe_position))
    stripe_turtle.pendown()
    stripe_turtle.begin_fill()
    stripe_turtle.forward(width)
    stripe_turtle.right(90)
    stripe_turtle.forward(stripe_width)
    stripe_turtle.right(90)
    stripe_turtle.forward(width)
    stripe_turtle.end_fill()
    next_stripe_position = next_stripe_position - stripe_width
    stripe_color = 1 if stripe_color == 0 else 0


# Canton Area
canton_turtle = te.Turtle()
canton_turtle.speed("fastest")
canton_turtle.penup()
canton_turtle.setpos((start_position, 450))
canton_turtle.pendown()
canton_turtle.color("#3C3B6E")
canton_turtle.begin_fill()
canton_turtle.forward(fly_of_the_canton)
canton_turtle.right(90)
canton_turtle.forward(489)
canton_turtle.right(90)
canton_turtle.forward(fly_of_the_canton)
canton_turtle.right(90)
canton_turtle.forward(489)
canton_turtle.end_fill()
canton_turtle.hideturtle()

# Prepare Star Turtle
stars = te.Turtle()
stars.speed("fastest")
stars.penup()
xcoord = -800
ycoord = 420
stars.goto(xcoord, ycoord)
stars.color("white")
# Draw six rows of stars (30 total)
for each_star in range(0, 30):
    stars.pendown()
    stars.begin_fill()
    xcoord = stars.xcor() + 60
    if xcoord >= -153.50:
        xcoord = -800
        ycoord = ycoord - 100
        stars.penup()
        stars.goto(xcoord, ycoord)
        stars.pendown()
    for i in range(5):
        stars.forward(30)
        stars.right(144)
        stars.forward(30)
        stars.right(72)
    stars.end_fill()
    stars.penup()
    stars.forward(110.5)
stars.hideturtle()

# Prepare for Alternate rows of Stars
sec_xcoord = -742.5
sec_ycoord = 370
stars.goto(sec_xcoord, sec_ycoord)
# Draw six rows of stars (20 total)
for each_star in range(0, 20):
    stars.pendown()
    stars.begin_fill()
    sec_xcoord = stars.xcor() + 60
    if sec_xcoord >= -153.50:
        sec_xcoord = -742.5
        sec_ycoord = sec_ycoord - 100
        stars.penup()
        stars.goto(sec_xcoord, sec_ycoord)
        stars.pendown()
    for i in range(5):
        stars.forward(30)
        stars.right(144)
        stars.forward(30)
        stars.right(72)
    stars.end_fill()
    stars.penup()
    stars.forward(110.5)
stars.hideturtle()

# Main Loop
te.done()
