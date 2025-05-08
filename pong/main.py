from turtle import Screen
from field import Field
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

field = Field()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

field.generate_field()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)  # screen.onkey nimmt funktionen nicht mit klammern!
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

while not score.end_game():  # man braucht die while loop, weil ...
    screen.update()  # ... der screen sich kontinuierlich updaten muss
    ball.forward(ball.move_speed)
    if ball.hits_upper_or_lower_sid():
        ball.bounce_from_screen()
    elif ball.xcor() >= 330 and right_paddle.distance(ball) <= 50 or \
            (ball.xcor() <= -330 and left_paddle.distance(ball) <= 50):
        ball.bounce_from_paddle()
        ball.move_speed += 0.1
    elif ball.scoring_player_1():
        score.update_score("left")
        ball.move("right")
    elif ball.scoring_player_2():
        score.update_score("right")
        ball.move("left")

screen.exitonclick()
