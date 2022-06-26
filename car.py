from turtle import Turtle
import random
import time

WIDTH = 600
HEIGHT = 600

colors = ['violet', 'red', 'orange', 'green', 'yellow', 'maroon']


class Car():
    def __init__(self):
        self.car_list = []
        self.min = 10
        self.max = 15

    def make_car(self):
        val = random.randint(1, 6)
        if val == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move(self):

        for car in self.car_list:
            car.penup()
            speed = random.randint(self.min, self.max)
            car.backward(speed)

    def collision(self, player):
        for car in self.car_list:
            if car.distance(player) < 23:
                text = Turtle()
                text.penup()
                text.write("Game Over!!!", align="center", font=("Courier", 24, "normal"))
                return True

    def increase_speed(self):
        self.min += 5
        self.max += 5