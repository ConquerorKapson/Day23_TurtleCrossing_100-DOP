import time
from turtle import Screen
from car import Car
from outcome import Score
from khilaadi import Player

WIDTH = 600
HEIGHT = 600
screen = Screen()

screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT)

car_list = []

car = Car()
score = Score()
kachua = Player()

screen.listen()
screen.onkeypress(kachua.go_up, "Up")

kachua.start()

game_is_on = True

while game_is_on:
    score.display_level()

    time.sleep(0.1)

    screen.update()

    car.make_car()
    car.move()

    if car.collision(kachua):
        game_is_on = False

    if kachua.ycor() >= 280:
        score.increase_level()
        kachua.start()
        car.increase_speed()

screen.exitonclick()
