import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

Level = 0
cars = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down' )

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car(Level)
    cars.move_car()
    for car in cars.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 300:
        player.goto(0, -280)
        cars.nextlevel()
        scoreboard.update_level()
        Level += 1

screen.exitonclick()