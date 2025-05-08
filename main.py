from random import randint
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=420, height=420)
# screen.tracer(0)
screen.title("Puzzle")
m = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
colors = {1: "red", 2: "orange", 3: "yellow", 4: "green",
          5: "red", 6: "orange", 7: "yellow", 8: "green",
          9: "red", 10: "orange", 11: "yellow", 12: "green",
          13: "red", 14: "orange", 15: "yellow"}

y_pos = 255

for i in range(3):
    x_pos = -155
    y_pos -= 100
    for j in range(4):
        print(numbers)
        m = randint(0, len(numbers)-1)
        print("m:", m)
        number = numbers[m]
        print(number)
        new_tile = Turtle(shape="square")
        new_tile.hideturtle()
        new_tile.color()
        new_tile.penup()
        new_tile.shapesize(4.5, 4.5)
        new_tile.setpos(x_pos,y_pos)
        new_tile.color(colors[number])
        new_tile.showturtle()
        new_number = Turtle()
        new_number.hideturtle()
        new_number.penup()
        new_number.setpos(x_pos, y_pos)
        new_number.write(number, font=("arial", 25, "bold"))
        x_pos += 100
        numbers.pop(m)
x_pos = -155
y_pos -= 100
for i in range(3):
    m = randint(0,len(numbers)-1)
    number = numbers[m]
    new_tile = Turtle(shape="square")
    new_tile.hideturtle()
    new_tile.color()
    new_tile.penup()
    new_tile.shapesize(4.5, 4.5)
    new_tile.setpos(x_pos, y_pos)
    new_tile.color(colors[number])
    new_tile.showturtle()
    new_number = Turtle()
    new_number.hideturtle()
    new_number.penup()
    new_number.setpos(x_pos, y_pos)
    new_number.write(number, font=("arial", 25, "bold"))
    x_pos += 100
    numbers.pop(m)



screen.listen()
screen.exitonclick()

