from turtle import Turtle, Screen
import random
colors = ["green yellow", "medium spring green", "deep sky blue", "magenta", "light sky blue", "medium turquoise"]
joginder = Turtle()
joginder.shape("turtle")
def draw_shape(n):
  angle = 360/n
  for _ in range(n):
    joginder.forward(100)
    joginder.right(angle)
for side in range(3,11):
  joginder.color(random.choice(colors))
  draw_shape(side)

screen = Screen()
screen.exitonclick() 