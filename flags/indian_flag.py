import turtle as te


screen_width = 2056
screen_height = 1329
flag_width = 900
flag_height = 600

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)


def jump(tobj, distanz):
    tobj.penup()
    tobj.forward(distanz)
    tobj.pendown()

def draw_band_line(band_turtle, distance, angle=0):
    band_turtle.forward(distance)
    band_turtle.right(angle)

def draw_spoke(spoke_turtle, distance, direction="right", angle=0):
    if direction == "left":
        # Left angle tilt
        spoke_turtle.left(angle)
    else:
        # Right angle tilt
        spoke_turtle.right(angle)
    # Distance to move forward from inside of center dot of Ashok Chakra to the edge of Inner white circle of Ashok Chakra.
    spoke_turtle.forward(distance)

# Initialize screen
screen = te.Screen()
te.title("Flag Of India")
# The width:height ratio is 3:2

# TODO Make screen_height and screen_width
# Setup turtle window in the center of screen.
# Add a 100 px
screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

# Orange Color
orange_band = te.Turtle()
# Adjust the Turtle speed
orange_band.speed('slow')
orange_band.penup()
orange_band.setpos((left_top_x, left_top_y))
orange_band.pendown()
orange_band.color("#FF9933", "#FF9933")
orange_band.begin_fill()
draw_band_line(orange_band, flag_width, 90)
draw_band_line(orange_band, flag_height / 3, 90)
draw_band_line(orange_band, flag_width, 90)
draw_band_line(orange_band, flag_height / 3, 0)
orange_band.end_fill()
orange_band.hideturtle()

# Calculate Green band position
# Postion = negative of (Half of flag height + Flag height divide by 3)
# As all three color bands are equally sized.

# Green Color
green_band = te.Turtle()
# Adjust the Turtle speed
# green_band.speed('fast')
green_band.penup()
green_band.setpos((left_top_x, -(left_top_y) + (flag_height / 3)))
green_band.pendown()
green_band.color("#138808", "#138808") 
green_band.begin_fill()
draw_band_line(green_band, flag_width, 90)
draw_band_line(green_band, flag_height / 3, 90)
draw_band_line(green_band, flag_width, 90)
draw_band_line(green_band, flag_height / 3, 0)
green_band.end_fill()
green_band.hideturtle()

# Ashok Chakra Start
outer_circle = te.Turtle()
# Adjust the Turtle speed
# outer_circle.speed('slow')
outer_circle.penup()
outer_circle.setpos((0, -(185 / 2)))
outer_circle.pendown()
outer_circle.color("#000080", "#000080")
outer_circle.begin_fill()
# Radius: 185 / 2
# TODO Make circle radius dynamic
outer_circle.circle(185 / 2)
outer_circle.end_fill()
outer_circle.setpos((0, -80))
outer_circle.hideturtle()


# Inner Circle
# Radius: (160 / 2)
inner_circle = te.Turtle()
# Adjust the Turtle speed
# inner_circle.speed('slow')
inner_circle.color("#ffffff", "#ffffff")
inner_circle.penup()
inner_circle.setpos((0, -80))
inner_circle.pendown()
inner_circle.begin_fill()
inner_circle.circle(80)
inner_circle.end_fill()
inner_circle.hideturtle()


# Center Dot
center_dot = te.Turtle()
# Adjust the Turtle speed
# center_dot.speed('slow')
center_dot.setpos((0, 0))
center_dot.dot(32, "navy")
center_dot.hideturtle()


spokes_turtle = te.Turtle()
# Adjust the Turtle speed
# spokes_turtle.speed('fast')
spokes_turtle.color('#000080', '#000080')
spoke_angel = 3.8
for i in range(24):
    spokes_turtle.seth(spoke_angel)
    # Go forward as per specification
    # TODO: Though this is hardcoded need to find a way to make this dynamic according to Ashok Chakra radius. Same for angle title and 
    spokes_turtle.forward(16.047)
    # Right side of spoke
    spokes_turtle.begin_fill()
    draw_spoke(spokes_turtle, 34, "right", 8.61)
    # Distance from this point to...
    # first_point = spokes_turtle.pos()
    draw_spoke(spokes_turtle, 34, "left", 8.61)
    spokes_turtle.left(180)
    # Left side of spoke
    draw_spoke(spokes_turtle, 34, "right", 8.61)
    # ...this point must be 6mm (or 6px) as described in specification.
    # You can print the distance here and check: print (spokes_turtle.distance(first_point))
    draw_spoke(spokes_turtle, 34, "left", 8.61)
    spokes_turtle.end_fill()
    spoke_angel = spoke_angel + 15
    spokes_turtle.setpos((0, 0))
    spokes_turtle.seth(0)
spokes_turtle.hideturtle()

radius = 80
dotted_circle = te.Turtle()
# Adjust the Turtle speed
# dotted_circle.speed('slow')
initial_angle = 0
initial_angle = initial_angle + 7.5
dotted_circle.seth(initial_angle)
for _ in range(24):
    jump(dotted_circle, radius)
    dotted_circle.pendown()
    dotted_circle.dot(7, "navy")
    jump(dotted_circle, -radius)
    initial_angle = initial_angle + 15
    dotted_circle.seth(initial_angle)
dotted_circle.hideturtle()

# Main Loop
te.done()
