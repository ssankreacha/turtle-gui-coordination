from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = Turtle()
for circles in range(72):
    tim.color(random.choice(colours))
    tim.speed("fastest")
    tim.circle(100)
    tim.left(5)


screen = Screen()
screen.exitonclick()
