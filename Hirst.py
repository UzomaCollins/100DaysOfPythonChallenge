# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('1.jpg', 80)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

colors_list = [(252, 251, 247), (253, 247, 250), (238, 252, 245), (248, 231, 27), (202, 12, 30), (238, 244, 250),
               (35, 91, 186),
               (232, 229, 4), (232, 149, 48), (197, 68, 22), (212, 13, 9), (35, 31, 152), (49, 220, 60), (241, 46, 151),
               (20, 22, 53),
               (14, 208, 224), (75, 9, 53), (17, 154, 18), (55, 26, 13), (80, 193, 223), (219, 23, 116), (232, 159, 8),
               (241, 64, 24),
               (221, 138, 191), (96, 75, 10), (247, 11, 9), (83, 238, 162), (11, 96, 63), (5, 35, 33), (89, 208, 147),
               (237, 158, 206),
               (86, 85, 205), (98, 225, 234), (251, 8, 15), (239, 168, 160), (177, 181, 222), (12, 246, 205),
               (15, 56, 244)] # RGB Colors

tim.setheading(230)
tim.forward(345)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
