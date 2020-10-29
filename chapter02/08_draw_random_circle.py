import random
import turtle

for i in range(0,10):
    radius = random.randint(5,100)
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(radius)

turtle.done()