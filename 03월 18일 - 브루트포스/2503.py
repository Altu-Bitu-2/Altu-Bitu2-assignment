import sys
from itertools import permutations
input=sys.stdin.readline

baseball=list(permutations(map(str,[1,2,3,4,5,6,7,8,9]),3))

#입력한 조건에 맞지 않은 수를 baseball에서 제거하는 함수
def strike_ball(num,strike,ball):
    global baseball
    num=str(num)
    temp=[] #baseball에서 제거할 수를 저장하는 리스트
    
    for i in baseball:
        s,b=strike,ball
        for j in i:
            if j in num:
                #strike인 경우
                if i.index(j)==num.index(j):
                    s-=1
                    continue
                #ball인 경우
                b-=1
        #조건에 맞지 않으면
        if s!=0 or b!=0:
            temp.append(i)
            
    for k in temp:
        baseball.remove(k)
            
                

n=int(input()) #질문 횟수
for _ in range(n):
    q,s,b=map(int,input().split())
    strike_ball(q,s,b)
    
print(len(baseball))
