import turtle as te

FLAG_NAME = "Flag Of Ukraine"

YELLOW_COLOR = "#FFD800"
STRONG_AZURE_COLOR = "#0056B9"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 3:2
flag_width = 1024
flag_height = 682.67

band_height = 0.5 * flag_height
band_width = flag_width

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

# Bring Window to front
# rootwindow = screen.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

screen.setup(canvas_width, canvas_height, int(((screen_width / 2) - (canvas_width / 2))),
             int((screen_height / 2) - (canvas_height / 2)))

azure_band = te.Turtle()
# azure_band.speed("fastest")
azure_band.penup()
azure_band.setpos(left_top_x, left_top_y)
azure_band.pendown()
azure_band.color("", STRONG_AZURE_COLOR)
azure_band.begin_fill()
azure_band.forward(band_width)
azure_band.right(90)
azure_band.forward(band_height)
azure_band.right(90)
azure_band.forward(band_width)
azure_band.right(90)
azure_band.forward(band_height)
azure_band.end_fill()
azure_band.hideturtle()

yellow_band = te.Turtle()
# yellow_band.speed("fastest")
yellow_band.penup()
yellow_band.setpos(left_top_x, left_top_y-band_height)
yellow_band.pendown()
yellow_band.color("", YELLOW_COLOR)
yellow_band.begin_fill()
yellow_band.forward(band_width)
yellow_band.right(90)
yellow_band.forward(band_height)
yellow_band.right(90)
yellow_band.forward(band_width)
yellow_band.right(90)
yellow_band.forward(band_height)
yellow_band.end_fill()
yellow_band.hideturtle()

name = te.Turtle()
# name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()