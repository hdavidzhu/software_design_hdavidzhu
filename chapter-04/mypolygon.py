from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
# print bob

# Draw a square.
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)

# for i in range(4):
#     print 'Hello!'

# for i in range(4):
#     fd(bob, 100)
#     lt(bob)

def square(t, length):  # t is a turtle
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):  # t is a turtle
    for i in range(n):
        fd(t, length)
        lt(t, 360.0/n)

def circle(t, r):
    circum = 2*pi*r
    resolution = 1000
    polygon(t, circum/resolution, resolution)

def arc(t, r, angle):
    circum = 2*pi*r
    resolution = 50
    for i in range(resolution * angle/360):
        fd(t, circum/resolution)
        lt(t, 360.0/resolution)

# square(bob, 100) 
# polygon(bob, 20, 30)
# circle(bob, 50)
# arc(bob, 50, 72)

# wait_for_user()