import turtle

radius = 50

turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.circle(radius)

turtle.up()
turtle.goto(100,0)
turtle.down()
radius += 20
turtle.circle(radius)

turtle.up()
turtle.goto(200,0)
turtle.down()
radius += 20
turtle.circle(radius)

turtle.done()