import sys
from heapq import *
input=sys.stdin.readline

n=int(input())
heap=[]

heap=list(map(int,input().split()))
heapify(heap)

for _ in range(n-1):
    temp=list(map(int,input().split())) 
    for i in temp:
        #윗줄에 있는 값이 아랫줄의 최솟값보다 크면
        if i>heap[0]:
            #힙에 큰값으로 채우기
            heappop(heap)
            heappush(heap,i)

print(heap[0])
