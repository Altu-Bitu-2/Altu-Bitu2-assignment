#BOJ11725 - 트리의 부모 찾기
import sys
from collections import *
input=sys.stdin.readline

#깊이 우선 탐색
def dfs(n):
    visited=[False]*(n+1)
    q=[] #스택
    q.append(1) #1부터 방문
    
    while q:
        curr=q.pop()
        visited[curr]=True

        #인접 노드 방문
        for next in adj_list[curr]:
            if not visited[next]:
                q.append(next)
                ans[next]=curr
                
n=int(input())
ans=[1]*(n+1) #부모 노드를 저장하는 리스트

#인접 리스트
adj_list=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs(n)
print(*ans[2:],sep='\n')
