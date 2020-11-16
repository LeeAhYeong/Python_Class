#1 : function (저효율) 
def circleArea(radius):
    print('반지름이',radius,'인 원의 면적: ', PI*radius*radius )

def circleCircumference(radius):
    print('반지름이',radius,'인 원의 둘레: ', 2*PI*radius )

PI = 3.1415926

radius = int(input('반지름의 값을 입력하세요: '))

circleArea(radius)
circleCircumference(radius)



#2 : function (고효율, 핵심 기능)

def circleArea(radius):
    return PI*radius*radius 

def circleCircumference(radius):
    return 2*PI*radius 

PI = 3.1415926

radius = int(input('반지름의 값을 입력하세요: '))

print('반지름이',radius,'인 원의 면적: ', circleArea(radius) )
print('반지름이',radius,'인 원의 둘레: ',  circleCircumference(radius))



#3 : global
def circleArea(radius):
    global PI
    global area

    area = PI * radius * radius
    
def circleCircumference(radius):
    global PI
    global circumference
    
    circumference = 2 * PI * radius

area = 0
circumference = 0
PI = 3.1415926
radius = int(input('반지름의 값을 입력하세요: '))
circleArea(radius)
circleCircumference(radius)
print('반지름이',radius,'인 원의 면적: ',area)
print('반지름이',radius,'인 원의 둘레: ',circumference)
