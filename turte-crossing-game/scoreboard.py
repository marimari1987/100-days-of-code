from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-200, 250)
        self.level = 1
        self.write(arg=f"Level: {self.level}", move=False, align= "center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align= "center", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=False, align= "center", font=FONT)

    def new_game(self):
        self.level = 1


