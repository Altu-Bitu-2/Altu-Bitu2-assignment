import sys #sys 모듈
input = sys.stdin.readline #입출력 향상 

"""
 [택시]

 graph : 플로이드-워셜 결과 행렬 그래프
 table : 경로표. table[i][j] = i->j로 가기 위해 제일 먼저 거쳐야 하는 정점

 1. i->j의 중간 경로를 i로 초기화
 2. i->k->j가 i->j보다 짧다면 i->j의 중간 경로를 i->k의 중간 경로(table[i][k])로 갱신
    k로 갱신하는게 아니라 table[i][k]로 갱신하는 이유는?
    만약 i->k의 경로가 i->t->k라면 최종 경로는 i->t->k->j
    바로 k로 갱신하면 t를 놓칠 수 있기 때문에 table[i][k]로 갱신
    line 24을 table[i][j] = k로 바꾸면 결과가 어떻게 되는지 확인해보세요
"""

def floyd_warshall(n, graph, table): #플로이드 워셜 함수
    for k in range(1, n+1): #k만큼 반복
        for i in range(1, n+1): #i만큼 반복
            for j in range(1, n+1): #j만큼 반복
                if graph[i][k] + graph[k][j] < graph[i][j]: #i->k->j 거친 경로가 i->j 보다 작으면
                    graph[i][j] = graph[i][k] + graph[k][j] #최단 경로 갱신
                    table[i][j] = table[i][k] #table 갱신
    return #함수 종료

INF = 10**5 * 2 #INF값 선언
n, m = map(int, input().split()) #n,m값 입력 받음
graph = [[INF]*(n+1) for _ in range(n+1)] #graph 선언
table = [[0]*(n+1) for _ in range(n+1)] #table 선언

for _ in range(m): #m만큼 반복
    a, b, s = map(int, input().split()) #a,b,s 값 입력 받음
    graph[a][b] = graph[b][a] = s #가중치 값 입력

    table[a][b] = b #최단 경로 입력
    table[b][a] = a #최단 경로 입력

floyd_warshall(n, graph, table) #플로이드 워셜 실생

for i in range(1, n+1): #1~n까지 반복
    table[i][i] = '-' #(i,i)에 - 입력

for line in table[1:]: #1~n까지 table의 행에서 
    print(*line[1:]) #행 출력