from turtle import Turtle


class Field:

    def generate_field(self):
        y_pos = -210
        for net_part in range(12):
            new_net = Turtle("square")
            new_net.penup()
            new_net.color("white")
            new_net.setposition(0, y_pos)
            new_net.shapesize(stretch_wid=1, stretch_len=0.25)
            y_pos += 40
