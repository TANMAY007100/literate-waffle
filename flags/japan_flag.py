import turtle as te

# Initialize screen
screen = te.Screen()
# The width:height ratio is 3:2
screen.setup(1200, 400)

red_circle = te.Turtle()
red_circle.color("#BE0028","#BE0028")
red_circle.begin_fill()
red_circle.dot(240)
red_circle.end_fill()
red_circle.hideturtle()

# Main Loop
te.done()