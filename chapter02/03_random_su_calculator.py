import random

num1 = random.randint(0,100)
num2 = random.randint(0,100)

answer = int(input(str(num1)+'-'+str(num2)+'='))

if num1-num2 == answer:
    print('맞았습니다.')
else:
    print('틀렸습니다.')