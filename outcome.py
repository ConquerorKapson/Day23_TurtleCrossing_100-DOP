from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def display_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.level += 1