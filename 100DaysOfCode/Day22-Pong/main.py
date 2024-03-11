from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

XMAX = 370
YMAX = 280

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong :: By Rajeshwaran")

right = Paddle(position=(380,0))
left = Paddle(position=(-380,0))
ball = Ball()
sb = Scoreboard()

screen.listen()
screen.onkey(right.move_up, "Up")
screen.onkey(right.move_down, "Down")
screen.onkey(left.move_up, "w")
screen.onkey(left.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()    

    if abs(ball.ycor()) > YMAX: # detect collision with top
        ball.bounce_y()
    
    if (ball.distance(right) < 50 and ball.xcor() > XMAX): # detect x and paddle hit        
        sb.update_right_score()
        ball.bounce_x()
    elif (ball.distance(left) < 50 and ball.xcor() < -1*XMAX):
        sb.update_left_score()
        ball.bounce_x()
    elif abs(ball.xcor() > XMAX):
        ball.reset_position()
    else:
        ball.move()

screen.exitonclick()