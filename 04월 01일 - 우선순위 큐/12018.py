import sys
import heapq as hq
input=sys.stdin.readline
n,m=map(int,input().split())
min_m=[]

for _ in range(n):
    p,l=map(int,input().split())
    m_temp=list(map(int,input().split()))
    mile=[]
    for i in m_temp:
        hq.heappush(mile,i)

    #수강인원이 찼으면 수강할 수 있는 최소 마일리지를 힙에 저장
    if p>=l: 
        for _ in range(p-l):
            hq.heappop(mile)
        hq.heappush(min_m,hq.heappop(mile)) 
    else: #수강인원이 다 안 찼으면
        hq.heappush(min_m,1)

cnt=0
#주어진 마일리지 범위에서 최대로 수강할 수 있는 강의 수 구하기
while m>0 and len(min_m)!=0:
    temp=hq.heappop(min_m)
    m-=temp

    if m<0:
        break
    cnt+=1
print(cnt) 
