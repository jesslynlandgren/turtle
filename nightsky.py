from turtle import *
from shapes import *
import random

bgcolor('#08182e')

speed(10)

for i in range(50):
    star(random.randint(1,25),True,'white')
    up()
    home()
    setheading(random.randint(0,360))
    forward(random.randrange(100,600,5))
    down()

mainloop()
