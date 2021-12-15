from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.level = 1
        self.goto(-200, 270)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center', font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align='center', font=FONT)