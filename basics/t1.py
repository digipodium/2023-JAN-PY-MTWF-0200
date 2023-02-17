from turtle import *

def square(d=100):
    for i in range(4):
        fd(d)
        lt(90)

def polygon(side=3, dis=50):
    for i in range(side):
        fd(dis)
        lt(360/side)

for i in range(3, 11):
    polygon(i, 100)
hideturtle()
mainloop()