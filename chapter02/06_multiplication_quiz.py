import random

while True:
    
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    answer = int(input(str(num1)+'*'+str(num2)+'는 '))

    if answer == num1*num2:
        print('맞았습니다.')
        break


