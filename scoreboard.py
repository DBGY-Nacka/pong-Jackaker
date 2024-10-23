from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, player1, player2):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.player1 = player1
        self.player2 = player2
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-140, 220)
        self.write(f"{self.player1}:{self.p1_score}",
                align="center",
                font=("Courier", 24, "normal")
                )
        
        self.goto(140, 220)
        self.write(f"{self.player2}:{self.p2_score}",
                align="center",
                font=("Courier", 24, "normal")
                )
        
        self.goto(0, 250)
        self.write(f"First to 11 wins!",
                align="center",
                font=("Courier", 24, "normal")
               )

    def p1_points(self):
        self.p1_score += 1
        self.update_score()

    def p2_points(self):
        self.p2_score += 1
        self.update_score()

    def declare_winner(self, winner_name):
        self.clear()
        self.goto(0, 0)
        self.write(f"{winner_name} Won!",
                   align = "center",
                   font = ("Courier", 36, "normal")
                   )
        
        self.goto(0, -50)
        self.write(f"{self.player1}:{self.p1_score} - {self.player2}:{self.p2_score}",
                   align = "center",
                   font = ("Courier", 24, "normal")
                   )