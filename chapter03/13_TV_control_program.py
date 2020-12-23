'''
1. state 자료형 해결
2. global 쓰임 해결
3. V/C 연산 후 범위 범주 해결
4. POINT 1~6 option? X > 처리
'''

def power():

    global state

    if state == False: 
        state = True
        print('전원 ON')
    else :
        state = False
        print('전원 OFF')

def setVolumnUp(size):

    global current_v_size 
    current_v_size += size

    if current_v_size <= 20:
        print(size,'만큼 볼륨을 올려 현재 볼륨',current_v_size,'입니다.')
    else:   
        current_v_size -= size
        print('더이상 높일 수 없습니다.')
        
    
def setVolumnDown(size):

    global current_v_size
    current_v_size += size

    if current_v_size >= 1:     
        print(size,'만큼 볼륨을 줄여서 현재 볼륨',current_v_size,'입니다.') 
    else:     
        current_v_size -= size
        print('더이상 볼륨을 줄일 수 없습니다.')

def setChannelUp(size):

    global current_c_size 
    current_c_size += size

    if  current_c_size <= 10:
        print('Channel',current_c_size)
    else:
        current_c_size -= size
        print('더이상 채널을 올릴 수 없습니다.')
               
    
def setChannelDown(size):

    global current_c_size
    current_c_size += size

    if current_c_size >= 1:
        print('Channel',current_c_size)      
    else:   
        current_c_size -= size
        print('더이상 채널을 내릴 수 없습니다.')
        
def getNow():

    if state == False:
        print('현재 전원: OFF상태 / 현재 볼륨:',current_v_size,'/ 현재 채널:',current_c_size)
    else:
        print('현재 전원: ON상태 / 현재 볼륨:',current_v_size,'/ 현재 채널:',current_c_size)

print('='*50)
print('1. 전원 끄기')
print('2. 전원 켜기')
print('3. 볼륨 조절')
print('4. 채널 조정')
print('5. 현재의 상태 출력')
print('6. 프로그램 종료')
print('='*50)

state = False # True, False (1byte) - 0,1 (4byte)
num = 0
size = 0
current_v_size = 0
current_c_size = 0

while(num != 6):

    num = int(input('원하는 기능의 번호를 입력하세요 >> '))

    if num == 1: #전원 끄기
        if state == 0:
            print('<이미 꺼져있습니다.>')
        else:
            power()

    elif num == 2: #전원 켜기
        if state == 1:
            print('<이미 켜져 있습니다.>')
        else:
            power()
    
    elif num == 3: #볼륨 조절
        if state == 0:
            print('<TV가 꺼져있습니다.>')  
        else:
            size = int(input('볼륨 조절: '))
            
            if size >= 0: #볼륨 업
                setVolumnUp(size)
            else: # 볼륨 다운
                setVolumnDown(size)

    elif num == 4: #채널 조절
        if state == 0:
            print('<TV가 꺼져있습니다.>') 
        else:
            size = int(input('채널 조절: '))
            
            if size >= 0: #볼륨 업
                setChannelUp(size)
            else: # 볼륨 다운
                setChannelDown(size)
    
    elif num == 5: #현재 상태 표시
        getNow()

    else:
        print('숫자를 잘 못 입력하셨습니다.') # 예외처리

print('프로그램을 종료합니다.')

        