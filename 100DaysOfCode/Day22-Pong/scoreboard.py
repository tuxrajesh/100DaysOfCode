from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()
    
    def update_score(self):
        self.clear()       
        self.write(f"Score: {self.left_score} | {self.right_score}", align=ALIGNMENT, font=FONT)

    def update_left_score(self):       
        self.left_score += 1
        self.update_score()
    
    def update_right_score(self):        
        self.right_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)