import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.cross_road)


def new_game():  #  alles bis auf die autos, die nicht verschwinden klappt immernoch
    car_manager.new_game()
    scoreboard.new_game()
    player.starting_position()
    game_is_on = True
    while game_is_on:  # quasi fertig
        time.sleep(0.1)
        car_manager.move_car()
        screen.update()
        car_manager.generate_car()
        for car in car_manager.cars:
            if player.distance(car) < 35 and car.ycor() - 10 < player.ycor() < car.ycor() + 10:
                # scoreboard write game Over
                game_is_on = False
        if player.finish():
            scoreboard.level_up()
            player.starting_position()
            car_manager.increase_speed()

    scoreboard.game_over()


screen.onkey(key="space", fun=new_game)

screen.exitonclick()
