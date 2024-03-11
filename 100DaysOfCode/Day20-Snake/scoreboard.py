from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self): 
        self.clear()       
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)