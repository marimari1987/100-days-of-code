import turtle
from turtle import *  # with the astrix everything gets imported
import random
# der große vorteil und ach nachteil ist, dass man nicht mehr z.B. random.coice schreiben muss
# der nachteil daran ist, dass man nicht mehr weiß wo z.B. choice() herkommt
# eine bessere Löung wäre z.B. import turtle as t, dann schreibt man t.Turtle()

timmy = Turtle()  # https://docs.python.org/3/library/turtle.html
timmy.shape("turtle")

# for i in range(4):  # timmy zeichnet eine gestrichelte linie im viereck
#     for side in range(5):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#     timmy.left(90)


# for x in range(3, 10):  # timmy malt verschiednene figuren in zufälligen farben
#     angle = 360/x
#     color = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
#     for site in range(x):
#         timmy.pencolor(color)  # color gibt die rgb werte wieder
#         timmy.forward(50)
#         timmy.left(angle)

# heading = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed(50)
#
# for step in range(100):  # timmy macht einen random walk
#     color = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
#     timmy.pencolor(color)
#     direction = random.choice(heading)
#     timmy.setheading(direction)
#     timmy.forward(20)

turtle.colormode(255)
timmy.speed(13)


def draw_spirograph(size_of_gap):
    for direction in range(10, 360, size_of_gap):  # range(start, ende, schritte)
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        timmy.pencolor(color)
        timmy.circle(100)
        timmy.setheading(direction)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

# import heroes  # packages, die noch nicht importiert wurden, werden rot unterlegt, klickt man darauf. kann man über
# # die rote lampe das package installieren lassem
# print(heroes.gen())
