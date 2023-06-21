import turtle as te


# Initialize screen
screen = te.Screen()
te.title("Flag Of Iceland")

# The width:height ratio is 25:18
flag_width = 1200
flag_height = 864

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

band_height = (11 / 100) * flag_height

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

left_band_point = (-(flag_width / 2), (5.55/100) * flag_height)
top_band_point = (left_top_x + ((32 / 100) * flag_width), (flag_height / 2))

blue_band = te.Turtle()
blue_band.penup()
# blue_band.speed("fastest")
blue_band.setpos(left_band_point)
blue_band.pendown()
blue_band.color("#DC1E35")
blue_band.begin_fill()
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(band_height)
blue_band.right(90)
blue_band.forward(flag_width)
blue_band.right(90)
blue_band.forward(band_height)
blue_band.end_fill()

blue_band.right(90)
blue_band.penup()
blue_band.setpos(top_band_point)
blue_band.pendown()
blue_band.color("#DC1E35")
blue_band.begin_fill()
blue_band.forward(band_height)
blue_band.right(90)
blue_band.forward(flag_height)
blue_band.right(90)
blue_band.forward(band_height)
blue_band.right(90)
blue_band.forward(flag_height)
blue_band.end_fill()
blue_band.hideturtle()

# Coordinates for each quadrant
right_top_x  = flag_width / 2
right_top_y  = flag_height / 2

left_bottom_x  = -(flag_width / 2)
left_bottom_y  = -(flag_height / 2)

right_bottom_x  = flag_width / 2
right_bottom_y  = -(flag_height / 2)

# 1st Quadrant Shape
# Right top shape in flag
# Drawing 1st quadrant shape
first_quadrant_shape = te.Turtle()
# first_quadrant_shape.speed("fastest")
first_quadrant_shape.penup()
first_quadrant_shape.setpos(right_top_x, right_top_y)
first_quadrant_shape.color("#02529C")
first_quadrant_shape.begin_fill()
first_quadrant_shape.pendown()
first_quadrant_shape.seth(180)
first_quadrant_shape.forward((56 / 100) * flag_width)
first_quadrant_shape.left(90)
first_quadrant_shape.forward((28 / 100) * flag_width)
# Uncomment the following line when checking point-to-point distance
# pt_in_1st_quadrant = first_quadrant_shape.pos()
first_quadrant_shape.left(90)
first_quadrant_shape.forward((56 / 100) * flag_width)
first_quadrant_shape.left(90)
first_quadrant_shape.forward((28 / 100) * flag_width)
first_quadrant_shape.left(90)
first_quadrant_shape.end_fill()
first_quadrant_shape.hideturtle()

# Left top shape in flag
# Drawing 2nd quadrant shape
second_quadrant_shape = te.Turtle()
# second_quadrant_shape.speed("fastest")
second_quadrant_shape.color("#02529C")
second_quadrant_shape.begin_fill()
second_quadrant_shape.penup()
second_quadrant_shape.setpos(left_top_x, left_top_y)
second_quadrant_shape.pendown()
second_quadrant_shape.forward((28 / 100) * flag_width)
second_quadrant_shape.right(90)
second_quadrant_shape.forward((28 / 100) * flag_width)
# The center imaginary shape formed between the edges of the four red shapes pointing towards the two bands crossing each other...
# must be a square i.e. all four distances between the points must of equal length
# Uncomment the following line to check the distance between 2nd point and 1st point
# print (f"Distance between point in the 2nd quadrant to point in 1st quadrant: {second_quadrant_shape.distance(pt_in_1st_quadrant)}")
# pt_in_2nd_quadrant = second_quadrant_shape.pos()
second_quadrant_shape.right(90)
second_quadrant_shape.forward((28 / 100) * flag_width)
second_quadrant_shape.right(90)
second_quadrant_shape.forward((28 / 100) * flag_width)
second_quadrant_shape.right(90)
second_quadrant_shape.end_fill()
second_quadrant_shape.hideturtle()

# Left bottom shape in flag
# Drawing 3rd quadrant shape
third_quadrant_shape = te.Turtle()
# third_quadrant_shape.speed("fastest")
third_quadrant_shape.penup()
third_quadrant_shape.setpos(left_bottom_x, left_bottom_y)
third_quadrant_shape.pendown()
third_quadrant_shape.color("#02529C")
third_quadrant_shape.begin_fill()
third_quadrant_shape.forward((28 / 100) * flag_width)
third_quadrant_shape.left(90)
third_quadrant_shape.forward((28 / 100) * flag_width)
# Uncomment the following line to check the distance between 3rd point and 1st point
# print (f"Distance between point in the 3rd quadrant to point in 1st quadrant diagonally: {third_quadrant_shape.distance(pt_in_1st_quadrant)}")
# Uncomment the following line to check the distance between 3rd point and 2nd point
# print (f"Distance between point in the 3rd quadrant to point in 2nd quadrant: {third_quadrant_shape.distance(pt_in_2nd_quadrant)}")
pt_in_3rd_quadrant = third_quadrant_shape.pos()
third_quadrant_shape.left(90)
third_quadrant_shape.forward((28 / 100) * flag_width)
third_quadrant_shape.left(90)
third_quadrant_shape.forward((28 / 100) * flag_width)
third_quadrant_shape.left(90)
third_quadrant_shape.end_fill()
third_quadrant_shape.hideturtle()

# Bottom right shape in flag
# Drawing 4th quadrant shape
fourth_quadrant_shape = te.Turtle()
# fourth_quadrant_shape.speed("fastest")
fourth_quadrant_shape.penup()
fourth_quadrant_shape.setpos(right_bottom_x, right_bottom_y)
fourth_quadrant_shape.color("#02529C")
fourth_quadrant_shape.begin_fill()
fourth_quadrant_shape.pendown()
fourth_quadrant_shape.seth(180)
fourth_quadrant_shape.forward((56 / 100) * flag_width)
fourth_quadrant_shape.right(90)
fourth_quadrant_shape.forward((28 / 100) * flag_width)
# Uncomment the following line to check the distance between 4th point and 1st point
# print (f"Distance between point in the 4th quadrant to point in 1st quadrant: {fourth_quadrant_shape.distance(pt_in_1st_quadrant)}")
# Uncomment the following line to check the distance between 4th point and 2nd point
# print (f"Distance between points in the 4th quadrant to point in 2nd quadrant diagonally: {fourth_quadrant_shape.distance(pt_in_2nd_quadrant)}")
# Uncomment the following line to check the distance between 4th point and 3rd point
# print (f"Distance between point in the 4th quadrant to point in 3rd quadrant: {fourth_quadrant_shape.distance(pt_in_3rd_quadrant)}")
fourth_quadrant_shape.right(90)
fourth_quadrant_shape.forward((56 / 100) * flag_width)
fourth_quadrant_shape.right(90)
fourth_quadrant_shape.forward((28 / 100) * flag_width)
fourth_quadrant_shape.right(90)
fourth_quadrant_shape.end_fill()
fourth_quadrant_shape.hideturtle()

# Uncomment to draw horizontal and vertical center lines and check
# measure = te.Turtle()
# measure.penup()
# measure.setpos(left_top_x, 0)
# measure.pendown()
# # Draw Horizontal and Vertically center lines
# # Set color to black
# measure.color("#000000")
# measure.forward(flag_width)
# measure.penup()
# measure.setpos(0, left_top_y)
# measure.pendown()
# measure.seth(270)
# measure.forward(flag_height)

te.done()