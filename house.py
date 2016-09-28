from turtle import *
from shapes import *



def houseSquare(size,fill2,color2):
    fill(fill2)
    color(color2)
    for i in range(4):
        forward(size)
        left(90)
    fill(False)


def houseRect(width,height,fill2,color2):
    fill(fill2)
    color(color2)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    fill(False)

speed(5)
bgcolor('#5f6c0e')

# Main House Block
up()
goto(-200,-200)
down()
setheading(0)
houseSquare(200,True,'white')

# Garage Block
(up)
goto(0,-200)
down()
setheading(0)
houseSquare(100,True,'white')

# Main House Roof
up()
goto(-200,0)
down()
setheading(0)
houseRect(200,50,True,'gray')

# Garage Roof
up()
goto(0,-100)
down()
setheading(0)
houseRect(100,50,True,'gray')

#Front Door
up()
goto(-125,-200)
down()
setheading(0)
houseRect(50,100,True,'brown')



mainloop()
