from turtle import Turtle
import random


class Food(Turtle):  # inheritance von Turtle

    def __init__(self):
        super().__init__()
        self.shape("circle")  # von der turtle superclass
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # normale göße 20 Pixel * 0,5
        self.color("red")
        self.speed("fastest")
        self.new_food()  # hier muss man aufpassen, weil z.B. self.reset(), würde die reset funktion aus turtle triggern

    def new_food(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)  # mit der goto funktion muss man kein neues Objekt erzeugen, es wandert einfach dorthin
