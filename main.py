import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

new_car = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_move()

    if new_car % 6 == 0:
        car.new_car()
