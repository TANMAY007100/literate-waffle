import turtle as te


def jump(tobj, distanz, winkel=0):
    tobj.penup()
    tobj.right(winkel)
    tobj.forward(distanz)
    tobj.left(winkel)
    tobj.pendown()

# Initialize screen
screen = te.Screen()
# The width:height ratio is 3:2
screen.setup(900, 600)

# Orange Color
t1 = te.Turtle()
t1.penup()
t1.setpos((-450, 300))
t1.pendown()
t1.color("#FF9933", "#FF9933") 
t1.begin_fill()
t1.forward(900)
t1.right(90)
t1.forward(200)
t1.right(90)
t1.forward(900)
t1.right(90)
t1.forward(200)
t1.end_fill()
t1.hideturtle()

# Green Color
t3 = te.Turtle()
t3.penup()
t3.setpos((-450, -100))
t3.pendown()
t3.color("#138808", "#138808") 
t3.begin_fill()
t3.forward(900)
t3.right(90)
t3.forward(200)
t3.right(90)
t3.forward(900)
t3.right(90)
t3.forward(200)
t3.end_fill()
t3.hideturtle()

# Ashok Chakra
t4 = te.Turtle()
t4.penup()
t4.setpos((0, -90))
t4.pendown()
t4.color("#000080", "#000080")
t4.begin_fill()
t4.circle(90)
t4.end_fill()
t4.setpos((0, -80))
t4.color("#ffffff", "#ffffff")
t4.begin_fill()
t4.circle(80)
t4.end_fill()
# Simple Spokes
t4.pencolor("navy")
t4.left(90)
t4.fd(160)
t4.setpos(0, 0)
for _ in range(23):
    t4.left(15)
    t4.fd(80)
    t4.bk(80)
# Center Dot
t4.setpos((0, 0))
t4.dot(28, "navy")
t4.hideturtle()

# Diamond Spokes
# starting_angle = 0
# t5 = te.Turtle()
# t5.setpos((1, 1))
# for each_spoke in range(0, 24):
#     t5.seth(starting_angle)
#     t5.begin_poly()
#     t5.color("navy", "navy")
#     t5.begin_fill()
#     t5.right(4)
#     t5.fd(40)
#     t5.left(5)
#     t5.fd(40)
#     t5.left(175)
#     t5.fd(40)
#     t5.left(5)
#     t5.fd(40)
#     t5.end_fill()
#     t5.end_poly()
#     starting_angle = starting_angle + 15
#     t5.goto(1, 1)
#     t5.seth(starting_angle)
# t5.hideturtle()

radius = 80
dotted_cricle = te.Turtle()
initial_angle = 7.5
dotted_cricle.left(initial_angle)
for _ in range(24):
    jump(dotted_cricle, radius)
    dotted_cricle.pendown()
    dotted_cricle.dot(8, "navy")
    jump(dotted_cricle, -radius)
    initial_angle = initial_angle + 15
    dotted_cricle.seth(initial_angle)
dotted_cricle.hideturtle()

# Main Loop
te.done()
