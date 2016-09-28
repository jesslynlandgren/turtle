from turtle import *

speed(10)

def equilateral(size, fill2, color2):
    setheading(60)

    fill(fill2)
    color(color2)
    for i in range(3):
        forward(size)
        right(120)
    fill(False)

def square(size, fill2, color2):
    fill(fill2)
    color(color2)
    for i in range(4):
        forward(size)
        left(90)
    fill(False)

def pentagon(size, fill2, color2):
    fill(fill2)
    color(color2)
    for i in range(5):
        forward(size)
        left(72)
    fill(False)

def hexagon(size, fill2, color2):
    fill(fill2)
    color(color2)
    for i in range(6):
        forward(size)
        left(60)
    fill(False)

def octogon(size, fill2, color2):
    fill(fill2)
    color(color2)
    for i in range(8):
        forward(size)
        left(45)
    fill(False)

def star(size, fill2, color2):
    fill(fill2)
    color(color2)
    for i in range(5):
        forward(size)
        right(144)
        forward(size)
        left(72)
    fill(False)

def circle2(size, fill2, color2):
    fill(fill2)
    color(color2)
    circle(size)
    fill(False)


if __name__ == '__main__':
    equilateral()
    square()
    pentagon()
    hexagon()
    octogon()
    star()
    circle2()

    mainloop()
