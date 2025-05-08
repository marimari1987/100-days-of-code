from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move("right")
        self.move_speed = 1.5

    def move(self, side):
        self.goto(0, 0)
        if side == "right":
            self.setheading(random.randint(10, 70))
        else:
            self. setheading(random.randint(170, 250))

    def scoring_player_2(self):
        if self.xcor() >= 400:  # screenwidth
            self.move_speed = 1.5
            print("scoring player 2")
            return True

    def scoring_player_1(self):
        if self.xcor() <= -400:
            self.move_speed = 1.5
            print("scoring player 1")
            return True

    def hits_upper_or_lower_sid(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            return True

    def bounce_from_screen(self):
        self.setheading(360 - self.heading())  # ball fliegt in die gegengesetzte richtung y-Achse
        # wenn man die bewegung mit der x und yachse machet, würde man das y *= -1 machen

    def bounce_from_paddle(self):
        self.setheading(180 - self.heading())  # ball fliegt in die gegengesetzte richtung x-Achse
        # wenn man die Bwegung mit der x und y achse machen würde, wäre x *= -1
