from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.score_1 = 0
        self.score_2 = 0
        self.write(arg=f"{self.score_1}   :   {self.score_2}", move=False, align="center", font=("arial", 18, "normal"))

    def update_score(self, player):
        if player == "left":
            self.score_2 += 1
            print(" score 2")
            print(self.score_2)
        elif player == "right":
            self.score_1 += 1
            print("score 1")
            print(self.score_1)
        self.clear()
        self.write(arg=f"{self.score_1}   :   {self.score_2}", move=False, align="center", font=("arial", 18, "normal"))

    def end_game(self):
        if self.score_1 == 5 or self.score_2 == 5:
            return True
        else:
            return False
