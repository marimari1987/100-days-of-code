from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        if random.randint(0, 5) == 1:
            y_pos = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setposition(300, y_pos)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -300:
                self.cars.remove(car)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def new_game(self):
        self.cars = []
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE = 5



