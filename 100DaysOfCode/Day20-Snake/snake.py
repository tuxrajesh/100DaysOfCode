STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SPEED = 'normal'

from turtle import Turtle

class Snake:
    def __init__(self):
        ''' initialize and create a snake '''
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        ''' create a snake with 3 segments '''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        ''' add a segment to the turtle at position '''
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        # new_segment.speed(SPEED)         
        self.segments.append(new_segment)

    def grow(self):
        ''' to grow the snake '''
        self.add_segment(self.segments[-1].position())

    def move(self):
        ''' move the snake forward '''
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        ''' change direction to UP '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        ''' change direction to DOWN '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        ''' change direction to LEFT '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        ''' change direction to RIGHT '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)