from turtle import Turtle
import turtle

screen=turtle.Screen()
MOVE_DISTANCE = 15
UP_LIMIT = 240
DOWN_LIMIT = -240

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)
        self.moving_up = False
        self.moving_down = False

    def up_press(self):
        if not self.moving_up:
            self.moving_up = True
            self.down_hold()

    def down_hold(self):
        if self.moving_up and self.ycor() < UP_LIMIT:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
            screen.ontimer(self.down_hold, 30)

    def stop_moving_up(self):
        self.moving_up = False

    def down_press(self):
        if not self.moving_down:
            self.moving_down = True
            self.dowm_hold()

    def dowm_hold(self):
        if self.moving_down and self.ycor() > DOWN_LIMIT:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
            screen.ontimer(self.dowm_hold, 30)

    def stop_moving_down(self):
        self.moving_down = False