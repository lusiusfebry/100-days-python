import turtle
from turtle import Turtle,Screen
from random import choice,randint

def main ():

    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)

    draw_spirograph(5)
    screen.exitonclick()

def draw_spirograph(size_of_gap):
    for i in range (int(360/size_of_gap)):
        turtle.speed("fastest")
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

def random_color():
    r  = randint(0,255)
    g = randint (0,255)
    b = randint (0,255)
    return (r,g,b)


main()


