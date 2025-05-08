from turtle import Screen
import time  # time erlaubt es einem das Programm langsamer anzuzeigen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.listen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # der tracer zeigt die einzelnen Schritte, das beduetet hier, amn sieht erst das erste segment
# wasnern, dann das zweite, sodass sich eine art raupenbewegung ergibt, was man nicht möchte

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

speed = 0.4
game_on = True
while game_on:
    screen.update()  # an dieser Stelle wird der progrmm prozess gezigt, sodass die zwischenschritte ausfallen
# und alle segmente sich gleichzeitig bewegen
    time.sleep(speed)  # macht Pause bis zur nähsten Codeausführung
    snake.move()
    if snake.head.distance(food) < 15:  # das food teilchen ist 10 pixel groß, mit etwas puffel 15 pixel Entfernung
        food.new_food()
        score.count()
        snake.extend_snake(snake.snake_segments[-1].xcor(), snake.snake_segments[-1].ycor())
    if snake.game_over():
        score.check_highscore()
        snake.reset()
        snake.move()


screen.exitonclick()
