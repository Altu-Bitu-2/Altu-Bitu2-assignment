import sys
import heapq as hq
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    k=int(input())
    temp=list(map(int,input().split()))
    chap=[]
    sum=0
    for i in temp:
        hq.heappush(chap,i)

    #파일이 하나로 합쳐질때까지 반복    
    while len(chap)!=1:
        cost=hq.heappop(chap)+hq.heappop(chap)
        sum+=cost
        hq.heappush(chap,cost)
    
    print(sum)
    
