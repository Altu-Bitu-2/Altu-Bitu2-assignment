import sys #sys 모듈
import heapq as hq #힙 가져오기
input = sys.stdin.readline #입출력 속도 향상

"""
 [특정한 최단 경로]

 가능한 경로
 1. 1 -> v1 -> v2 -> n
 2. 1 -> v2 -> v1 -> n
 -> 1, v1, v2를 시작점으로 하는 다익스트라 함수 실행하기

 !주의!
 한 번 이동했던 정점, 간선을 다시 방문할 수 있음. 즉 1->N의 최댓값이 INF(1e5*8)이 아니라 3*INF!
"""

INF = 8*(10**5) * 3   # 최대 N-1개의 간선을 지나게 됨 * 중복 순회 가능(3)

def dijkstra(n, graph, start): #다익스트라 
    dist = [INF]*(n+1) #최단 경로 값 저장하는 리스트
    pq = [(0, start)] #(0,시작 정점) 힙에 삽입

    dist[start] = 0 #시작 정점 가중치

    while pq: #힙이 빌 때까지
        weight, curr = hq.heappop(pq) #현재 정점의 가중치, 현재 정점
        if weight > dist[curr]: #현재 가중치가 최소가 아니면
            continue #다음 반복문으로
        for next, next_weight in graph[curr]: #다음 정점, 다음 정점의 가중치에 대해 반복
            new_weight = next_weight + weight #현재 가중치와 다음 정점의 가중치를 더함
            if new_weight < dist[next]: #새로 계산한 가중치가 최소이면
                dist[next] = new_weight #새로 계산한 가중치로 업데이트
                hq.heappush(pq, (new_weight, next)) #(새로 계산한 가중치, 정점) 힙에 삽입

    return dist #dist 리스트 반환


n, e = map(int, input().split()) #n,e값 입력 받기
graph = [[] for _ in range(n+1)] #graph 선언

for _ in range(e): #e만큼 반복
    a, b, c = map(int, input().split()) #a,b,c 입력 받음
     #(정점, 거리) 저장
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split()) #반드시 지나야 하는 정점 값 입력 받음

dist = [] #최단 경로 배열 선언
for s in (1, v1, v2): #1,v1,v2 각각을 시작 정점으로 다익스트라 실행
    dist.append(dijkstra(n, graph, s)) #다익스트라 결과값을 dist에 저장

# 1->v1->v2->n의 경로와 1->v2->v1->n의 경로 중 최솟값
# 무방향 그래프기 때문에 v1->v2와 v2->v1은 사실 같은 값!
ans = min(dist[0][v1] + dist[1][v2] + dist[2][n], dist[0][v2] + dist[2][v1] + dist[1][n]) #최소인 경로를 ans에 저장

if ans >= INF: #결과가 INF보다 크거나 같으면
    print(-1) #경로 없음
else: #경로가 있으면
    print(ans) #정답 출력