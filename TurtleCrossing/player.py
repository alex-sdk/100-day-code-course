from turtle import Turtle

from car_manager import MOVE_INCREMENT
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
       super().__init__()
       self.penup()
       self.setheading(90)
       self.goto(STARTING_POSITION)
       self.shape('turtle') 
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)