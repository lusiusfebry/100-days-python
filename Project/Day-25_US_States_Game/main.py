from turtle import Turtle,Screen
import pandas
turtle = Turtle()
screen = Screen()
screen.title("U.S State Game")
image = "blank.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print (x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
#
#
#
# turtle.mainloop() #keep screen open


data = pandas.read_csv("50_states.csv")
# data_state = data["state"].to_list()
all_state = data.state.to_list()

guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50", prompt="What's the another state : ").title()

    if answer_state == "Exit" :
        missing_sate = [state for state in all_state if state not in guess_states]
        # for state in all_state:
        #     if state not in guess_states:
        #         missing_sate.append(state)
        new_data = pandas.DataFrame(missing_sate)
        new_data.to_csv("missing_state.csv")


        break
    if answer_state in all_state:
        guess_states.append(answer_state)
        t= Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.state.item())


#build the missing state not in guess state list and save to csv file
# state_to_learn = []
# for state in all_state:
#     if state not in guess_states:
#         state_to_learn.append(state)
#
#
# panda_data_frama = pandas.DataFrame(state_to_learn)
# panda_data_frama.to_csv("testtt.csv"
#                         "")