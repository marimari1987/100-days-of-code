from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 250)
        self.color("white")
        self.hideturtle()
        self.score = -1
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.count()

    def count(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Your score: {self.score} High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGN, font=FONT)

    def check_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))  # kann man auch als f string konvertieren
            self.score = 0
        else:
            self.score = 0
        self.update()




