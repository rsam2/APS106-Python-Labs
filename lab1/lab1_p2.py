# APS106 Lab 1 - Drawing Shapes with Turtle



################################################
# Part 2 - Draw your initials
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()


# use alex to draw your first and last initials
# TODO: WRITE YOUR CODE HERE

#reposition alex to start at the bottom left of uppercase R
alex.setheading(180)            #make alex face west
alex.up()                       #make alex put pen up
alex.forward(200)               #make alex go 200 forward without drawing
alex.left(90)                   #make alex turn left 90 degrees
alex.forward(150)               #make alex go 150 forward without drawing
alex.right(180)                 #make alex turn right 180 degrees

#draw R
alex.down()                     #make alex put pen down
alex.forward(250)               #make alex move forward 300
alex.left(90)                   #make alex turn left 90 degrees
alex.forward(-20)               #make alex move right 20
alex.circle(90, -180)           #make alex go in a circle of radius 90 for -180 degrees
alex.forward(-20)               #make alex move right 20
alex.right(40)                  #make alex turn right 80 degrees
alex.forward(90)                #make alex move forward 90
alex.up()                       #make alex put pen up

#reposition to bottom of S
alex.setheading(0)              #make alex face east
alex.forward(200)               #make alex move forward 100

#draw S
alex.down()                     #make alex put pen down
alex.forward(30)                #make alex go forward 30
alex.circle(70, 120)            #make alex go in a circle of radius 70 for 120 degrees
alex.setheading(180)            #make alex face west
alex.right(10)                  #make alex turn right 10 degrees
alex.forward(60)                #make alex move forward 60
alex.setheading(0)              #make alex face east
alex.circle(70, -240)           #make alex go in a circle of radius 70 for -240 degrees



turtle.done()
