x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

x3 = int(input('x3: '))
y3 = int(input('y3: '))

import turtle

turtle.up()
turtle.goto(x1,y1)
turtle.down()

turtle.goto(x2,y2)
turtle.goto(x3,y3)

turtle.done()