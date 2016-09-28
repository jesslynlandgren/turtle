from turtle import *
from draw_a_square import draw_square

coord_list = [(-100,-100,100),(100,100,200),(-100,100,120),(100,-100,250)]

speed(1)

for coord in coord_list:
    up()
    home()
    x, y, size = coord
    setheading(0)
    forward(x)
    setheading(90)
    forward(y)
    down()
    draw_square(size)

mainloop()
