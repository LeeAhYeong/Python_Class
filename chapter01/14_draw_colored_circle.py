import turtle  # 질문 할것 

radius = 100
color_list = []

for _ in range(4) :
    color = input("색깔 >> ")
    color_list.append(color)

for i in range(4) :

    turtle.fillcolor(color_list[i])
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    turtle.goto((i+1)*100,0)
    turtle.down()
  
turtle.done()

