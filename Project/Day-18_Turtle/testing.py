from turtle import Turtle,Screen

turtle = Turtle()
# turtle.penup()
turtle.speed("fastest")

turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(0)


screen = Screen()
# print (screen.screensize())
screen.exitonclick()

