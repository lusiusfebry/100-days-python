from turtle import Turtle,Screen
from random import choice,randint
def main ():

    turtle = Turtle()
    turtle.shape("turtle")
    # turtle.color("red","black")
    screen = Screen()
    screen.colormode(255)
    colors = ["DarkSeaGreen","cyan","Red","beige","coral","DeepPink","Chocolate","blue1"]
    direction = [0,90,180.270,260]
    turtle.pensize(15)
    for i in range (200):
        turtle.color(random_color())
        turtle.forward(30)
        turtle.seth(choice(direction))
        turtle.speed(10)




    screen.exitonclick()

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random = (r,g,b)
    return random



main()


