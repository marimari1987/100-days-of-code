from turtle import Turtle


class Paddle(Turtle):  # ohne dass man Paddle eine Subklasse von Turtle macht...
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.position = position
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(position)

    def move_up(self):  # ... funktionieren diese Funktionen nicht
        self.goto(self.xcor(), self.ycor() + 30)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 30)


