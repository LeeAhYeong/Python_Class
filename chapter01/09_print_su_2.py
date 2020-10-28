num = int(input("정수를 입력하세요 : ")) #1234

total = 0

total += num // 1000     # 1
num = num % 1000         # 234

total += num // 100      # 2
num = num % 100          #34

total += num // 10       # 3
total += num % 10        # 4

print("자리수의 합 : ", total)