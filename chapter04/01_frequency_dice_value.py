import random as r

count = [0,0,0,0,0,0]

for _ in range (1000):

    su = r.randint(1,6)

    if su == 1:
        count[0] += 1

    elif su == 2:
        count[1] += 1

    elif su == 3:
        count[2] += 1

    elif su == 4:
        count[3] += 1
       
    elif su == 5:
        count[4] += 1
    
    else :
        count[5] += 1
        
for i in range (1,7):

    print('주사위가',i,'인 경우는',count[i-1])
    
