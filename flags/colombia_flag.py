import turtle as te

FLAG_NAME = "Flag Of Colombia"

# Initialize screen
screen = te.Screen()
te.title(FLAG_NAME)

# The width:height ratio is 3:2
flag_width = 1200
flag_height = 800

canvas_width = flag_width + 100
canvas_height = flag_height + 200

left_top_x = -(flag_width / 2)
left_top_y = (flag_height / 2)

screen_height = int((screen.window_height() + 0.75) / 0.75)
screen_width = screen.window_width() * 2

screen.setup(canvas_width, canvas_height, ((screen_width / 2) - (canvas_width / 2)), (screen_height / 2) - (canvas_height / 2))

amarillo_yellow_band_height = 0.5 * flag_height
azul_blue_rojo_red_band_height = 0.25 * flag_height

amarillo_yellow_color = "#FCD116"
azul_blue_color = "#003893"
rojo_red_color = "#CE1126"

def draw_band(tobj: te.Turtle, height, width, pos_x, pos_y, color):
    tobj.showturtle()
    tobj.penup()
    tobj.setpos(pos_x, pos_y)
    tobj.seth(0)
    tobj.pendown()
    tobj.color("", color)
    tobj.begin_fill()
    tobj.forward(width)
    tobj.right(90)
    tobj.forward(height)
    tobj.right(90)
    tobj.forward(width)
    tobj.right(90)
    tobj.forward(height)
    tobj.end_fill()
    tobj.hideturtle()
    return pos_x, pos_y

flag = te.Turtle()
x_pos, y_pos = draw_band(flag, amarillo_yellow_band_height, flag_width, left_top_x, left_top_y, amarillo_yellow_color)
x_pos, y_pos = draw_band(flag, azul_blue_rojo_red_band_height, flag_width, x_pos, y_pos - amarillo_yellow_band_height, azul_blue_color)
x_pos, y_pos = draw_band(flag, azul_blue_rojo_red_band_height, flag_width, x_pos, y_pos - azul_blue_rojo_red_band_height, rojo_red_color)


name = te.Turtle()
name.speed("fastest")
name.penup()
name_location = (0, 0 - (flag_height / 2) - 60)
name.setpos(name_location)
name.pendown()
name.write(FLAG_NAME, move=False, align="center", font=("Arial", 40, "bold"))
name.hideturtle()

te.done()