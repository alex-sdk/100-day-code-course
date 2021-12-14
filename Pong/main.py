from time import sleep
from turtle import Screen, width
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, 'Up')
screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle1.go_down, 'Down')
screen.onkey(paddle2.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 30 and ball.xcor() > 340 or ball.distance(paddle2) < 30 and ball.xcor() > -340:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_Postion()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_Postion()
        scoreboard.r_point()

screen.exitonclick()
