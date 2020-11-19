start = int(input('시작 수: '))
end = int(input('끝 수: '))
plus_su = int(input('증가 값: '))

print('합:',end='')
total = 0
total_2 = 1
for i in range(start,end+1,plus_su):
    total += i
    print(i, '+ ',end = '') 
     
print("\b\b=",total) 

print('곱:',end='')
for i in range(start,end+1,plus_su):
    total_2 *= i 
    print(i, '* ',end = '') 

print("\b\b=",total_2)