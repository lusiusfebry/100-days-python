from turtle import Turtle,Screen
from random import choice
def main ():

    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color("red","black")
    colors = ["DarkSeaGreen","cyan","Red","beige","coral","DeepPink","Chocolate","blue1"]
    direction = [0,90,180.270,260]
    turtle.pensize(15)

    for i in range (200):
        turtle.color(choice(colors))
        turtle.forward(30)
        turtle.seth(choice(direction))
        turtle.speed(10)



    screen = Screen()
    screen.exitonclick()



main()


