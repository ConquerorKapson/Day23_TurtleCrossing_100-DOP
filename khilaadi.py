from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()

    def start(self):
        self.goto(0, -280)

    def go_up(self):
        self.fd(10)

