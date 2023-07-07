from turtle import Turtle
from player import Player
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_chance = random.randint(1, 6)
        if car_chance == 6:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y_position = random.randint(-250, 250)
            car.goto(x=280, y=random_y_position)
            self.cars.append(car)

    def move_car(self):
        for cars in self.cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


