import sys
from heapq import *
input=sys.stdin.readline

n=int(input())
time=[]
room=[]
for _ in range(n):
    s,t=map(int,input().split())
    time.append((s,t))
time.sort(key=lambda x:(x[0],x[1])) #start,end 기준 정렬

heappush(room,time[0][1]) #end값 
for t in time[1%n:n]:
    #수업 시작 전보다 일찍 끝난 수업이 있으면
    if room[0]<=t[0]:
        heappop(room)
        heappush(room,t[1])
    else: heappush(room,t[1])

print(len(room))
    


        
