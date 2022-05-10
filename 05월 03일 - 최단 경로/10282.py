import sys
from heapq import *
input=sys.stdin.readline
INF=1e9

#다익스트라
def dijkstra(start,n,graph):
    dist=[INF for _ in range(n+1)]
    dist[start]=0
    heap=[]
    heappush(heap,(0,start))

    #(간선의 가중치, 간선의 번호)
    while heap:
        curr_weight,curr_idx=heappop(heap)
        for next in graph[curr_idx]:
            next_idx,next_weight=next
            if dist[next_idx]<next_weight: 
                continue
            temp=curr_weight+next_weight
            if temp<dist[next_idx]:
                dist[next_idx]=temp
                heappush(heap,(temp,next_idx))
    return dist
            
#a가 b를 의존한다 => b->a 방향의 간선
t=int(input())
for _ in range(t):
    n,d,c=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    cnt,final_sec=0,0 #감염된 컴퓨터 개수, 컴퓨터가 마지막으로 감염된 시간]
    #그래프 생성
    for _ in range(d):
        a,b,s=map(int,input().split())
        graph[b].append((a,s))

    dist=dijkstra(c,n,graph)
    for d in dist:
        if d==INF: 
            continue
        else:
            cnt+=1
            final_sec=max(final_sec,d)
    print(cnt,final_sec)