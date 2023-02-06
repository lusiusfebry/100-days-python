from turtle import Turtle,Screen

def main ():

    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color("red","black")
    turtle.c
    # print(turtle.position())
    # draw_square(turtle)
    # draw_dashed_line(turtle)
    draw_different_shape(turtle)
    screen = Screen()
    screen.exitonclick()

def draw_square(turtle):
    for _ in range (4):
        turtle.forward(100)
        turtle.left(90)

def draw_dashed_line (turtle):
    for i in range (15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_different_shape (turtle):
    for side in range (3,11):
        for i in range ():
            angle = 360 / i
            turtle.forward(100)
            turtle.right(angle)




main()


