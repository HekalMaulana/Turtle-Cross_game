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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for cars in car.cars:
        if player.distance(cars.pos()) < 30:
            scoreboard.game_over()
            game_is_on = False

    if player.finis_line():
        player.start_position()
        car.level_up()
        scoreboard.increase_score()


screen.exitonclick()
