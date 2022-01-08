from turtle import Screen
from snack_for_part_2 import Snack
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The snack game")
screen.tracer(0)
screen.listen()

snack = Snack()
screen.onkey(snack.up, key="Up")
screen.onkey(snack.down, key="Down")
screen.onkey(snack.left, key="Left")
screen.onkey(snack.right, key="Right")

again = True
while again:
    screen.update()
    time.sleep(0.1)
    snack.move()

screen.exitonclick()