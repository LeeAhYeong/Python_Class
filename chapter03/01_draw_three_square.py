import turtle

def square():
    for _ in range (0,4): # 0,1,2,3
        turtle.forward(50) 
        turtle.left(90)
    
for _ in range(3) :
    square()
    turtle.up()
    turtle.forward(50+20)
    turtle.down()

turtle.done()