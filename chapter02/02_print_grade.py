score = int(input('성적을 입력하시오: '))

if score >= 90:
    print('A학점입니다.')
elif 80 <= score < 90:
    print('B학점입니다.')
elif 70 <= score < 80:
    print('C학점입니다.')
elif 60 <= score < 70:
    print('D학점입니다.')
elif score < 60:
    print('F학점입니다.')
