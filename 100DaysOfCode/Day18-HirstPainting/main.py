###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
import turtle as t
import random as rnd

rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# colors = colorgram.extract('Day18-HirstPainting\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
pupu = t.Turtle()
t.colormode(255)
pupu.speed('fast')
pupu.penup()
x = -200.0
y = -200.0
position = (x, y)
for row in range(10):
      
    pupu.goto(position)
    for col in range(10):
        pupu.dot(15, rnd.choice(rgb_colors))
        pupu.forward(50)
    position = (x, pupu.position()[1] + 50)

screen = t.Screen()
screen.exitonclick()