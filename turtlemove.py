import sys
from random import randint
from turtle import forward, left, speed

speed('slowest')
for idx, argument in enumerate(sys.stdin):
    if idx == 0:
        # In case of the first argument -the Python program name- do nothing in
        # this iteration, jump over it with `continue`
        continue

    turtle_steps = int(argument)
    forward(turtle_steps)

    random_angle = randint(45, 135)
    left(random_angle)