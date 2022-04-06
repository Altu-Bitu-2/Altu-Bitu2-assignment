import sys
from collections import deque
import heapq as hq
input=sys.stdin.readline
n,m,k=map(int,input().split())
wait=[deque() for _ in range(m)] #n명 사원 정보 저장 리스트
first=[] #선두 정보 저장하는 리스트 
for i in range(n):
    d,h=map(int,input().split())
    wait[i%m].append((-d,-h,i%m))

deka_line=k%m
deka_turn=k//m+1
cnt=0

for i in range(m):
    if wait[i]:
        hq.heappush(first,wait[i].popleft())
        
#데카의 순서가 올때까지 반복
while deka_turn>0:
    temp=hq.heappop(first)
    if temp[2]==deka_line:
        deka_turn-=1
        if deka_turn!=0: #아직 데카 차례가 아니면
            cnt+=1
    else:
        cnt+=1
        
    if wait[temp[2]]:
        hq.heappush(first,wait[temp[2]].popleft())

print(cnt)
    
    
    


