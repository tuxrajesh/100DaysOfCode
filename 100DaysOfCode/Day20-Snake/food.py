from turtle import Turtle
import random

class Food(Turtle):
    ''' food for the snake '''

    def __init__(self):
        ''' init food instance '''
        super().__init__()        
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.move()

    def move(self):
        ''' move the food to a random position '''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)