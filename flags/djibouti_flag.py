import turtle as te

# Initialize screen
screen = te.Screen()
te.title("Flag Of Djibouti")

# The width:height ratio is 3:2
flag_width = 1280
flag_height = 853.33

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

# Blue Band
band_turtle = te.Turtle()
# band_turtle.speed("fast")
band_turtle.penup()
band_turtle.color("", "#6AB2E7")
band_turtle.setpos(left_top_x, left_top_y)
band_turtle.pendown()
band_turtle.begin_fill()
band_turtle.forward(flag_width)
band_turtle.right(90)
band_turtle.forward(flag_height / 2)
band_turtle.right(90)
band_turtle.forward(flag_width)
band_turtle.right(90)
band_turtle.forward(flag_height / 2)
band_turtle.end_fill()

# Green Band
# band_turtle.speed("fast")
band_turtle.penup()
band_turtle.color("", "#12AD2B")
band_turtle.setpos(left_top_x, 0)
band_turtle.seth(0)
band_turtle.pendown()
band_turtle.begin_fill()
band_turtle.forward(flag_width)
band_turtle.right(90)
band_turtle.forward(flag_height / 2)
band_turtle.right(90)
band_turtle.forward(flag_width)
band_turtle.right(90)
band_turtle.forward(flag_height / 2)
band_turtle.end_fill()
band_turtle.hideturtle()

equilateral_triangle = te.Turtle()
# equilateral_triangle.speed("fast")
equilateral_triangle.penup()
equilateral_triangle.color("", "#FFFFFF")
equilateral_triangle.setpos(left_top_x, left_top_y)
equilateral_triangle.begin_fill()
equilateral_triangle.pendown()
equilateral_triangle.right(30)
equilateral_triangle.forward(flag_height)
equilateral_triangle.right(120)
equilateral_triangle.forward(flag_height)
equilateral_triangle.end_fill()
equilateral_triangle.hideturtle()

# The star center is located at 22.13% of flag width
star_center = 0.2213 * flag_width

# Height of Star
height_of_star = 0.246 * flag_height
# Side Of Star point
side_of_star = (height_of_star / 0.9511) / 2.618

star = te.Turtle()
# Vertex of equilateral triangle
star.penup()
star.color("#D7141A")
star.setpos(left_top_x, 0)
star.forward(star_center)
star.seth(90)
star.forward(height_of_star / 2)
star.pendown()
star.seth(0)
star.begin_fill()
star.right(72)
for _ in range(5):
    star.forward(side_of_star)
    star.left(72)
    star.forward(side_of_star)
    star.right(144)
star.end_fill()
star.hideturtle()


te.done()