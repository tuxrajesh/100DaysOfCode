import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

is_game_on = True
guesses = []
while is_game_on:
    q_title = f"{len(guesses)}/50 states correct"
    answer = screen.textinput(title=q_title, prompt="What's another state's name?")
    
    if(answer == None):
        is_game_on = False
        break

    answer = answer.title()
    if answer in all_states:        
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        choice_state_data = data[data.state == answer]
        t.goto(int(choice_state_data.x), int(choice_state_data.y))
        t.write(choice_state_data.state.item())
        guesses.append(answer)    
    is_game_on = len(guesses) < 50

missing_states = [state for state in all_states if state not in guesses]
new_csv = pandas.DataFrame(missing_states)
new_csv.to_csv("tolearn.csv")

screen.exitonclick()