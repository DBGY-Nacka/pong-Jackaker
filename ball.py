from turtle import Turtle
import random
import time

paddle_bounce_cooldown = time.time()

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set_random_heading()

    def set_random_heading(self):
        angle = random.choice([random.randint(-45, 45), random.randint(135, 225)])
        self.setheading(angle)

    def move(self):
        self.forward(1)

    def border_bounce(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def paddle_bounce(self):
        """Makes sure that ball does not bounce multiple times on the 
           same paddle if it hits the paddles at the top or bottom since
           the hitbox is messured from the paddles center"""
        global paddle_bounce_cooldown
        if time.time()-paddle_bounce_cooldown > 0.5:
            self.setheading(180-self.heading())
            paddle_bounce_cooldown=time.time()

    def reset_position(self):
        self.goto(0, 0)
        self.set_random_heading()
