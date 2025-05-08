from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
i = 0

def move_forwards():
    timmy.forward(10)


def counter_clock_wise():
    timmy.setheading(timmy.heading()+10)


def clock_wise():
    timmy.setheading(timmy.heading()+350)


def backwards():
    timmy.backward(10)


def clear():
    timmy.reset()


def change_color():
    global i
    colors = ["black", "red", "yellow", "green", "blue", "orange", "purple"]
    if i > 6:
        i = 0
    else:
        timmy.color(colors[i])
        timmy.pencolor(colors[i])
        i += 1

#screen.listen()  # event listener
# screen.onkey(key="space", fun=move_forwards)  # hier bruacht man keine Klammern um die funkton abzurufen siehe auch calculator
# # higher order function (funktionen, die von funktionen abgerufen werden)
# screen.exitonclick()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)
screen.onkey(key="space", fun=change_color)
screen.exitonclick()

