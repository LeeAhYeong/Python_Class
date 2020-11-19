#도형 그리는 기능을 함수로 구현하지 않은 경우
# random 이어야 할것: 색깔, 길이, 몇각형인지, 위치(x,y)
import random as r
import turtle as t

color_list = ['yellow', 'white', 'green', 'blue', 'red', 'orange', 'purple']

for i in range (10):

    length = r.randint(10,100)
    sides = r.randint(3,10)
    x = r.randint(-200,200)
    y = r.randint(-200,200)

    t.up()
    t.goto(x,y)
    t.down()

    t.fillcolor(color_list[r.randint(0,6)])
    t.begin_fill()

    for _ in range (sides):  # 다각형 도형 하나 그리기
        t.forward(length)
        t.left(360//sides)

    t.end_fill()

t.done()


#도형 그리는 기능을 함수로 구현한 경우

import random as r
import turtle as t

color_list = ['yellow', 'white', 'green', 'blue', 'red', 'orange', 'purple']

def draw_shape(color,length,sides,x,y):

    t.up()
    t.goto(x,y)
    t.down()

    t.fillcolor(color)
    t.begin_fill()

    for _ in range (sides):  # 다각형 도형 하나 그리기
        t.forward(length)
        t.left(360//sides)

    t.end_fill()

for i in range (10):

    color = color_list[r.randint(0,6)]
    length = r.randint(10,100)
    sides = r.randint(3,10)
    x = r.randint(-250,250)
    y = r.randint(-250,250)

    draw_shape(color,length,sides,x,y)
    
t.done()

