from turtle import Turtle
LENGTH = 5
WIDTH = 1

class Paddle (Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH,stretch_len=LENGTH)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        ''' move up '''
        self.forward(50)

    def move_down(self):
        ''' move down '''
        self.back(50)
    
