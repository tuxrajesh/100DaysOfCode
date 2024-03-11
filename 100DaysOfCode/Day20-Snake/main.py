SCREEN_EDGE = 280

from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake :: Sssshhhh!")

snake = Snake()
food = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    # detection with food; increase score
    if snake.head.distance(food) < 20:
        sb.update_score()
        food.move()
        snake.grow()

    # detection with wall; game end
    if abs(snake.head.xcor()) > SCREEN_EDGE or abs(snake.head.ycor()) > SCREEN_EDGE:
        game_is_on = False
        sb.game_over()

screen.exitonclick()