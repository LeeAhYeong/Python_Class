'''
(1) turtle.color('red')  -> 선과 칠하는 색 모두 빨간색  
    turtle.color('red','blue') -> 선의 색: 빨간색 칠하는 색: 파란색 

(2) tutle.pencolor('red') -> 선의 색만 빨간색
    tutle.fillcolor('red') -> 칠하는 색만 빨간색
    
 * 주의 사항: begin_fill() 그리고 end_fill()과 같이 써야함   
예) turtle.fillcolo('red')
    turtle.begin_fill()  
    도형 그리기
    turtle.end_fill()        '''

import turtle as t

def draw_bar(height):

    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill() # 도형 그리고 색칠 완료 

    t.left(90) # 화살표 위치 재조정
    t.forward(width)

t.color('blue','red')
height_list = [120,66,309,220,156,23,98]
width = 30

for i in range (0,7): #0,1,2,3,4,5,6
    draw_bar(height_list[i])
    
#for detail in data : # for 변수 in [120,56,309,220,156,23,98]
#    drawBar(detail)

t.done()