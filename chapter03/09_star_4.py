num = int(input('정수를 입력하시오: '))

for i in range (1,num+1):
    for j in range(i):
        print(' ',end = '')
    for j in range(num-i):
        print('*',end = '')
    
    print()