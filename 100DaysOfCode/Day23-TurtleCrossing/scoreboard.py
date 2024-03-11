from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_score()

    def update_score(self): 
        self.clear()       
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.score += 1

