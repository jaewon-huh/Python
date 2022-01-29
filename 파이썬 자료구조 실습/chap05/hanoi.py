# 하노이의 탑 구현하기 

def move(no,x,y) :
    """ 원반 no개를 x 기둥에서 y기둥으로 옮김"""

    if no >1 : 
        move(no-1, x, 6-x-y )       # 중간기둥 2 으로 옮김 

    print(f'원반 [{no}]를 {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no >1 : 
        move(no-1, 6-x-y, y)
# 재귀 
n = int(input('원반의 개수를 입력하세요 : '))

move(n,1,3)

''' move(3,1,3) :
    1단계 move(2,1,2) -- 
                    1단계 : move(1,1,3) : 원반 1을 1기둥에서 3기둥으로 옮깁니다.
                    2단계 : 원반 2를 1기둥에서  2기둥으로 옮깁니다. 
                    3단계 : move(1,3,2) : 원반 1을 3기둥에서 2기둥으로 옮깁니다. 
    2단계 원반 3을 1기둥에서 3기둥으로 옮깁니다 . 
    3단계 move(2,2,3) ...
    
'''