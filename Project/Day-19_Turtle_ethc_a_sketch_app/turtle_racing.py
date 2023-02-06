from turtle import Turtle,Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle win the race ? input color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
y_index = -100
for turtle_index in range (6):
    y_index += 30
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(-230, y_index)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print (f"You've won! The {winning_color} turtle is the wiiner!")
            else:
                print (f"You've lost! The {winning_color} turlte is the winner")

        random_distant = randint(0,10)
        turtles.forward(random_distant)



screen.exitonclick()
