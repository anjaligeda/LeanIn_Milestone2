import turtle
import math
wn = turtle.Screen()
wn.bgcolor("white")
triangle = turtle.Turtle()
triangle.color("black")
triangle.shape("arrow")
triangle.fillcolor("black")

triangle.begin_fill()
triangle.forward(100) # draw base
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
 

triangle.end_fill()
