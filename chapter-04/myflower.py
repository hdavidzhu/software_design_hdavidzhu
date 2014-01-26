from swampy.TurtleWorld import *
from math import pi
from math import sin
from math import radians
from myflower import *

world = TurtleWorld()
bob = Turtle()
# bob.delay = 0.001
bob.delay = 0.1

def polyline(turtle, length, sides, sidenumber):
    """
    Draws a partial polygon.

    turtle = given turtle instance.
    length = length of side.
    sides = number of sides on the polygon.
    sidenumber = how many sides to draw.
    """
    for i in range(sidenumber):
        fd(turtle, length)
        lt(turtle, 360.0/sides)

def polygon(turtle, length, sides):
    """
    Draws a whole polygon.
    
    turtle = given turtle instance.
    length = length of side.
    sides = number of sides on the polygon.
    """
    polyline(turtle = turtle, length = length, sides = sides, sidenumber = sides)

def arc(turtle, radius, angle):
    """
    Draws an arc.
    
    turtle = given turtle instance.
    radius = radius of circle of arc.
    angle = how munch of the arc to draw.
    """
    circumference = 2 * pi * radius
    resolution = int(circumference / 2) + 1
    polyline(turtle = turtle, length = circumference / resolution, sides = resolution, sidenumber = int(resolution * angle / 360))

def pedal(turtle, radius, angle):
    """
    Draws a pedal of a flower.

    turtle = given turtle instance.
    radius = radius of the arcs.
    angle = angle between the arcs.
    """
    for i in range(2):
        arc(turtle = turtle, radius = radius, angle = angle)
        lt(turtle, 180 - angle)

def flower(turtle, radius, angle, budnumber):
    """
    Draws a flower.

    turtle = given turtle instance.
    radius = radius of the outer flower.
    budnumber = how many buds to draw.
    """
    for i in range(budnumber):
        pedal(turtle = turtle, radius = radius, angle = angle)
        lt(turtle, 360.0 / budnumber)

def isosceles(turtle, radius, angle):
    """
    Creates a isosceles triangle.

    turtle = given turtle instance.
    radius = length of equal sides.
    angle = angle between two equal lengths.
    """
    end_angle = (180.0 - angle) / 2.0
    outer_end_angle = 180 - end_angle
    edge_length = radius * (sin(radians(angle)) / sin(radians(end_angle)))
    # print end_angle
    # print outer_end_angle
    # print edge_length

    fd(turtle, radius)
    lt(turtle, outer_end_angle)
    fd(turtle, edge_length)
    lt(turtle, outer_end_angle)
    fd(turtle, radius)
    lt(turtle, 180.0 - angle)

def pie(turtle, radius, pienumber):
    """
    Draws a polygon with divisions of pie.

    turtle = given turtle instance.
    radius = distance of polygon corner to center.
    pienumber = number of slices.
    """
    for i in range(pienumber):
        isosceles(turtle, radius, 360.0 / pienumber)
        lt(turtle, 360.0 / pienumber)


# arc(bob, 50, 180)
# arc(bob, 60, 360)
# pedal(bob, 60, 100)
# flower(bob, 1000, 10, 10)
# isosceles(bob, 100, 40)
pie(bob, 100, 6)
wait_for_user()