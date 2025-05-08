from turtle import Turtle

MOVE_DISTANCE = 20  # Constants werden groß geschrieben und kommen gnz nach oben, damit man nicht suchen muss
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for square in range(3):
            self.extend_snake(x, y)
            x -= 20

    def extend_snake(self, x, y):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.setposition(x, y)
        self.snake_segments.append(new_square)

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):  # von hinten schauen sich die segmente
            # das jeweils vordere an und folgen
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SOUTH:  # die Schlange darf nicht in die Entgegengesetzte Richtung gehen
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def game_over(self):
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= - 300:
            return True

    def reset(self):
        for segment in self.snake_segments:  # ohne jedes segment anzusprechen,geht es nicht
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]  # man muss nochmal das gleiche machen wie zum initalisieren
