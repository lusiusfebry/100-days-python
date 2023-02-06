import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    # turtle.left(90)
    # print (turtle.heading())
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def turn_right():
    # turtle.right(90)
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
