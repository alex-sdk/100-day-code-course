from turtle import Turtle, screensize

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=0, y= 270)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def Refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)
