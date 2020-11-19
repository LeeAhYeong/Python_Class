su_list = []

def maxvalue(su_list):
    n = len(su_list)
    max_su = su_list[0]
    
    for i in range (0,n):
        if su_list[i] >= max_su:
            max_su = su_list[i]
    
    return max_su

def minvalue(su_list):
    n = len(su_list)
    min_su = su_list[0]
    
    for i in range (0,n):
        if su_list[i] <= min_su:
            min_su = su_list[i]
    
    return min_su
    
for i in range (1,11):
    su = int(input(str(i)+'번째 숫자를 입력하시오 >> '))
    su_list.append(su)
    maxvalue(su_list)
    minvalue(su_list)

print('입력된 값은',su_list,'이며,\n제일 큰 값은',maxvalue(su_list),'이고,\n제일 작은 값은',minvalue(su_list),'이다.')


