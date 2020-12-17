# import colorgram
import random
import turtle

# --------------Code below only run once to get the colors from image.

# colors = colorgram.extract('Kirby.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# ----------------Code about only run once to get the colors from image.

color_list = [(250, 209, 237), (156, 52, 133), (230, 119, 181), (164, 17, 107), (98, 170, 228), (207, 155, 95),
              (78, 76, 167), (97, 104, 192), (187, 229, 249), (241, 160, 216), (211, 82, 136), (227, 218, 93),
              (246, 231, 197), (94, 199, 106), (60, 40, 157), (221, 247, 234), (55, 173, 109), (140, 106, 66),
              (43, 136, 86), (146, 140, 84), (175, 178, 232), (108, 230, 162), (251, 223, 0), (102, 220, 245),
              (202, 98, 80), (248, 165, 148), (42, 172, 203), (142, 37, 29), (14, 108, 62), (38, 10, 104)]

# -----------------------Code below for dot painting

# timmy = turtle.Turtle()
# turtle.colormode(255)
# timmy.penup()
# turtle_xpos = -300
# turtle_ypos = -300
# timmy.hideturtle()
#
#
# def draw_forward():
#     for _ in range(10):
#         color = random.choice(color_list)
#         timmy.dot(40, color)
#         timmy.forward(65)
#
#
# for i in range(10):
#     timmy.setpos(turtle_xpos, turtle_ypos)
#     draw_forward()
#     turtle_ypos += 65

# --------------------Code about for dot painting

angle = 0
timmy = turtle.Turtle()
timmy.hideturtle()
turtle.colormode(255)
turtle.hideturtle()
timmy.speed('fastest')


for i in range(36):
    timmy.color(random.choice(color_list))
    timmy.setheading(angle)
    timmy.circle(150)
    angle += 10


screen = turtle.Screen()
screen.exitonclick()
