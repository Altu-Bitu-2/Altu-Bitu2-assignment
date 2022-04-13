import sys
import heapq as hq
input=sys.stdin.readline
n=int(input()) #방문 횟수
gift=[]
for _ in range(n):
    line=list(map(int,input().split()))
    #선물 가치 저장한 최대힙 생성
    for i in line[1::]:
        hq.heappush(gift,-i)
        
    if line[0]==0:
        if len(gift)==0:
            print(-1)
        else:
            print(-hq.heappop(gift))
