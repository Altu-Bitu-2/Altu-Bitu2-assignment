from collections import deque
n,m=map(int,input().split())
do,su,do_ground,su_ground=deque(),deque(),deque(),deque()

#누가 이겼는지 판단하는 함수
def who_is_win(do,su):
    if len(do)>len(su):
        return 'do'
    elif len(do)<len(su):
        return 'su'
    else:
        return 'dosu'

#초기 카드 세팅
for _ in range(n):
    do_card,su_card=map(int,input().split())
    do.appendleft(do_card)
    su.appendleft(su_card)

#게임 진행
turn='do'
for i in range(m):
    if turn=='do':
    #도도가 카드 내려놓음
        do_ground.append(do.popleft())
        turn='su'
        if len(do)==0:
            break
        #도도가 종을 침
        elif do_ground[-1]==5:
            do+=su_ground+do_ground
            su_ground.clear()
            do_ground.clear()
            continue
        #수연이 종을 침
        elif len(su_ground)!=0 and do_ground[-1]+su_ground[-1]==5:
            su+=do_ground+su_ground
            su_ground.clear()
            do_ground.clear()
            continue
        continue
    
    elif turn=='su':  
    #수연이 카드 내려놓음
        su_ground.append(su.popleft())
        turn='do'
        if len(su)==0:
            break
        #도도가 종을 침
        elif su_ground[-1]==5:
            do+=su_ground+do_ground
            su_ground.clear()
            do_ground.clear()
            continue
        #수연이 종을 침
        elif len(do_ground)!=0 and do_ground[-1]+su_ground[-1]==5:
            su+=do_ground+su_ground
            su_ground.clear()
            do_ground.clear()
            continue

print(who_is_win(do,su))
