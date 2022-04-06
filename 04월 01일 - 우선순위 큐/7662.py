import sys
input=sys.stdin.readline
from heapq import *
SIZE=1000001
max_q=[]
min_q=[]

#다른힙에서 지워진 값을 지우는 함수
def remove_ano(heap,remove):
    #다른 힙에서 제거한 값이면
    while heap and not remove[heap[0][1]]:
        heappop(heap)
               
t=int(input())
for _ in range(t):
    k=int(input())
    remove=[False for _ in range(SIZE)]
    for i in range(k):
        cmd=input().split()
        #삽입 연산
        if cmd[0]=='I':
            heappush(max_q,(-int(cmd[1]),i))
            heappush(min_q,(int(cmd[1]),i))
            remove[i]=True

        #삭제 연산
        elif cmd[0]=='D':
            if cmd[1]=='1': #최댓값 제거
                remove_ano(max_q,remove)
                if max_q:
                    remove[heappop(max_q)[1]]=False

            elif cmd[1]=='-1': #최솟값 제거
                remove_ano(min_q,remove)
                if min_q:
                    remove[heappop(min_q)[1]]=False
                                        
    remove_ano(min_q,remove)
    remove_ano(max_q,remove)
    
    if not min_q or not max_q:
        print('EMPTY')
    else:
        print(-max_q[0][0],min_q[0][0])
