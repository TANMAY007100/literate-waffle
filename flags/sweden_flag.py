import turtle as te


# Initialize screen
screen = te.Screen()
te.title("Flag Of Sweden")

# The width:height ratio is 8:5
flag_width = 1280
flag_height = 800

canvas_width = flag_width + 100
canvas_height = flag_height + 100

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

# Width of Vertical band is 20 percent of Flag Height
vertical_band_width = 0.2 * flag_height
# Width of Horizontal band is 12.5 percent of Flag Width
horizontal_band_width = 0.125 * flag_width

left_band_point = (-(flag_width / 2), (20/100) * (flag_height / 2))
top_band_point = (left_top_x + ((31.25 / 100) * flag_width), (flag_height / 2))

blue_field = te.Turtle()
# blue_field.speed("fastest")
blue_field.penup()
blue_field.setpos(left_top_x, left_top_y)
blue_field.pendown()
blue_field.color("#016AA9")
blue_field.begin_fill()
blue_field.forward(flag_width)
blue_field.right(90)
blue_field.forward(flag_height)
blue_field.right(90)
blue_field.forward(flag_width)
blue_field.right(90)
blue_field.forward(flag_height)
blue_field.right(90)
blue_field.end_fill()
blue_field.hideturtle()


yellow_band = te.Turtle()
# yellow_band.speed("fastest")
# Draw Horizontal band
yellow_band.penup()
yellow_band.setpos(left_band_point)
yellow_band.pendown()
yellow_band.color("#FDCD00")
yellow_band.begin_fill()
yellow_band.forward(flag_width)
yellow_band.right(90)
yellow_band.forward(horizontal_band_width)
yellow_band.right(90)
yellow_band.forward(flag_width)
yellow_band.right(90)
yellow_band.forward(horizontal_band_width)
yellow_band.end_fill()
# Draw Vertical band
yellow_band.right(90)
yellow_band.penup()
yellow_band.setpos(top_band_point)
yellow_band.pendown()
yellow_band.begin_fill()
yellow_band.forward(vertical_band_width)
yellow_band.right(90)
yellow_band.forward(flag_height)
yellow_band.right(90)
yellow_band.forward(vertical_band_width)
yellow_band.right(90)
yellow_band.forward(flag_height)
yellow_band.end_fill()
yellow_band.hideturtle()

# Uncomment to measure distance to check 
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
# # Check Left top corner
# # Width must be 31.25 percent of flag width
# # Height must be 40 percent of flag height
# measure.penup()
# measure.setpos(left_top_x, left_top_y)
# measure.pendown()
# measure.seth(0)
# measure.forward(0.3125 * flag_width)
# measure.right(90)
# measure.forward(0.4 * flag_height)
# measure.right(90)
# measure.forward(0.3125 * flag_width)
# measure.right(90)
# measure.forward(0.4 * flag_height)
# measure.right(90)

te.done()