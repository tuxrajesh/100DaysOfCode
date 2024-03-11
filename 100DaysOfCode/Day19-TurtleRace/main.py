from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "green", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80]
all_turtles = []

for index in range(0, 5):
    trtl = Turtle(shape="turtle")
    trtl.penup()
    trtl.color(colors[index])
    trtl.goto(x=-230, y=y_positions[index])
    all_turtles.append(trtl)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle(random.randint(0, 20))
        if turtle.xcor() >= 200:
            is_race_on = False

winner_pos = 0
winner_color = ""
for turtle in all_turtles:
    if turtle.xcor() > winner_pos:
        winner_pos = turtle.xcor()
        winner_color = turtle.pencolor()

if winner_color == user_bet:
    print("You win!")
else:
    print(f"You lose. Winning turtle: {winner_color}")
    
    



screen.exitonclick()