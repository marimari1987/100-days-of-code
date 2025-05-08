from turtle import Turtle, Screen, textinput
import pandas

data_file = pandas.read_csv("/absolute_path")
data = pandas.DataFrame(data_file)
states_list = data.state.to_list()
# print(int(data[data.state == "Alabama"].x))

screen = Screen()
image = "/absolute_path/blank_states_img.gif"
screen.bgpic(image)
screen.setup(width=730, height=500)
screen.title("US States Names Quiz")

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

remaining_states = len(states_list)

while len(states_list) > 0:
    new_state = textinput(f"Name a State{50-remaining_states}/{remaining_states} remaining", "Which State do you know?").title()
    if new_state == "exit":
        pandas.DataFrame(states_list).to_csv("states_to_learn.csv")
        break
    if new_state in states_list:
        x_pos = int(data[data.state == new_state].x)
        y_pos = int(data[data.state == new_state].y)
        turtle.setposition(x_pos, y_pos)
        turtle.write(new_state)
        states_list.remove(new_state)
        remaining_states -= 1

screen.exitonclick()
