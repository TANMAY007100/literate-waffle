import turtle as te
import math

def draw_tangent(turtle_obj):
    start_point = turtle_obj.pos()
    pt_line = te.Turtle()
    pt_line.speed("fastest")
    pt_line.penup()
    pt_line.color("#FFCCDD")
    pt_line.setpos(start_point)
    pt_line.seth(turtle_obj.heading())
    pt_line.down()
    pt_line.forward(200)
    pt_line.hideturtle()

def draw_five_pointed_star(tobj: te.Turtle, n_vertices, radius, x_coord, y_coord, fill_color="#FFFFFF", pen_color="", speed="normal"):
    tobj.showturtle()
    phi = round((1 + math.sqrt(5)) / 2, 4)

    pentagon_edge_length = 2 * (radius * math.sin(math.radians(36)))
    side = pentagon_edge_length / phi

    tobj.speed(speed)
    tobj.penup()
    tobj.setpos(x_coord, y_coord)
    tobj.setheading(90)
    tobj.right((2 * math.pi) / n_vertices * (180 / math.pi))
    
    vertex_angle = 360 / n_vertices
    outer_start_angle = 2 * vertex_angle
    tobj.forward(radius)
    tobj.setheading(0)
    tobj.right(outer_start_angle)

    tobj.pendown()
    if pen_color or fill_color:
        tobj.color(pen_color, fill_color)
    tobj.begin_fill()
    for _ in range(0, n_vertices):
        tobj.forward(side)
        # Uncomment to draw tangents to verify shape geometry.
        # Note: This is currently designed for pentagon star only.
        # draw_tangent(tobj)
        tobj.left(outer_start_angle - vertex_angle)
        tobj.forward(side)
        tobj.right(outer_start_angle)
    tobj.end_fill()
    tobj.penup()
    tobj.hideturtle()
