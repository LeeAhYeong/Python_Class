num = int(input("정수를 입력하시오: "))

for i in range(1,num+1,2) :
  for j in range((num-i)//2) :
    print(" ", end="")
  for j in range(i) :
    print("*", end="")
  print()

for i in range(num, 1, -2) :
  for j in range((num-i)//2) :
    print(" ", end="")
  for j in range(i-1) :
    print("*", end="")
  print()

'''
            0   *       i
0000*       4   1       0   5-(i+1) = 4
000***      3   3       1   5-(i+1) = 3
00*****     2   5       2   5-(i+1) = 2
0*******    1   7       3   5-(i+1) = 1
*********   0   9       4   5-(i+1) = 0
                2*n-1
*********   0   9       4
0*******    1   7       3
00*****     2   5       2
000***      3   3       1
0000*       4   1       0
'''