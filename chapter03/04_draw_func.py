# x축과 y축을 먼저 그리기
import turtle

turtle.forward(100)
turtle.forward(-100)
turtle.left(90)
turtle.forward(100)
turtle.forward(-100)

def func(x):
    return x**2 + 1

for x in range(0,101):
    turtle.goto(x,func(x)*0.01)

turtle.done()