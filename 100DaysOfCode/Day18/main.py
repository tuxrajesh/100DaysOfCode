import turtle as trl
import random

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_shape(t, no_of_sides, steps):
    angle = 360/no_of_sides
    for _ in range(no_of_sides):
        t.forward(steps)
        t.right(angle)

def random_walk():
    tim = trl.Turtle()
    trl.colormode(255)
    tim.pensize(15)
    colors = ['red', 'orange', 'cyan', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'lime', 'blue violet']
    # for no_of_sides in range(3, 11):
    #     tim.color(random.choice(colors))
    #     draw_shape(tim, no_of_sides, 100)

    directions = [0, 90, 180, 270]

    for _ in range(100):
        tim.color(get_random_color())
        tim.forward(25)
        tim.setheading(random.choice(directions))

def draw_spirograph():
    tim = trl.Turtle()
    tim.speed('fastest')
    trl.colormode(255)

    for _ in range(25):        
        tim.color(get_random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + 15)

random_walk()
# draw_spirograph()

# Keep the screen on
screen = trl.Screen()
screen.exitonclick()