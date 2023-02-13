import random
from turtle import Turtle, Screen

tim = Turtle()
tim.speed('fastest')

# def draw_spiralgraph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random.choice(color))
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# print(draw_spiralgraph(5))

tim.colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


for _ in range(50000):
    tim.forward(30)
    tim.color((random.choice(random_color())))
    tim.setheading(random.choice(directions))

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(color))
#     draw_shape(shape_side_n)

# for _ in range(4):
#     tinny_the_turtle.forward(100)
#     tinny_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
