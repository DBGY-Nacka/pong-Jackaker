from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

winning_point = 11

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

text_player1 = screen.textinput("Player 1", "Name player 1:")
text_player2 = screen.textinput("Player 2", "Name player 2:")

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))

ball = Ball()
scoreboard = Scoreboard(text_player1, text_player2)

screen.listen()
screen.onkeypress(left_paddle.up_press, "w")
screen.onkeyrelease(left_paddle.stop_moving_up, "w")
screen.onkeypress(left_paddle.down_press, "s")
screen.onkeyrelease(left_paddle.stop_moving_down, "s")

screen.onkeypress(right_paddle.up_press, "Up")
screen.onkeyrelease(right_paddle.stop_moving_up, "Up")
screen.onkeypress(right_paddle.down_press, "Down")
screen.onkeyrelease(right_paddle.stop_moving_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.border_bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 350) or\
        (ball.distance(left_paddle) < 50 and ball.xcor() < -350):
        ball.paddle_bounce()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.p1_points()
        time.sleep(0.5)
        left_paddle.goto(-370, 0)
        right_paddle.goto(370, 0)
        
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.p2_points()
        time.sleep(0.5)
        left_paddle.goto(-370, 0)
        right_paddle.goto(370, 0)
        
    if scoreboard.p1_score >= winning_point:
        game_is_on = False
        scoreboard.declare_winner(text_player1)

    if scoreboard.p2_score >= winning_point:
        game_is_on = False
        scoreboard.declare_winner(text_player2)

screen.exitonclick()
