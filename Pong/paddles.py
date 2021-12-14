from turtle import Turtle, pos

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=0.25)
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
            new_y = self.ycor() + 35
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)