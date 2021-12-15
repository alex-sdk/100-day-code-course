from turtle import Turtle
import random
from typing import NewType

COLORS = ["red", "orange", "cyan", "green", "blue", "purple"]
starting_move_increment = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.car_list = []
        
    def create_car(self, level):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            rand_y = random.randint(-280, 280)
            rand_x = random.randint(225, 280)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(rand_x, rand_y)
            self.car_list.append(new_car)    
            new_car.speed = starting_move_increment + (MOVE_INCREMENT * level)
                
    def move_car(self):
        for car in self.car_list:
            car.forward(car.speed)

    def nextlevel(self):
        for car in self.car_list:
            car.goto(-330, 0)
        self.car_list.clear()
        
        
