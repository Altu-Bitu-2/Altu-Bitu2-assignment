import sys #sys 모듈
input = sys.stdin.readline #입출력 향상 코드

"""
[도시 분할 계획]

마을을 두개로 분리하고, 각 집끼리 이동할 수 있는 최소한의 도로만 남기는 문제
즉, 2개의 최소신장트리를 만들어야 하는 문제
-> 하나의 최소신장트리를 만들고, 그 중 가장 유지비가 큰 도로를 삭제
-> 크루스칼 알고리즘에서 가장 마지막에 삭제되는 도로가 유지비가 가장 큼
-> 크루스칼 알고리즘에서 간선을 n-2개만 선택하여 그 합을 구하여 해결
"""

# find 연산
def find_parent(x):
    if parent[x] < 0: #x가 루트 노드면
        return x #x 반환
    
    parent[x] = find_parent(parent[x]) #루트 노드 찾아서 parent[x]에 대입
    return parent[x] #parent[x] 반환

# union 연산
def union(x, y):
    px = find_parent(x) #x의 부모 노드 찾아서 대입
    py = find_parent(y) #y의 부모 노드 찾아서 대입

    if px == py: #동일한 루트 노드면
        return False #합칠 수 없음
    
    if parent[px] < parent[py]: #py가 더 적은 자식 노드 가지면
        parent[px] += parent[py] #py를 px에 합침
        parent[py] = px #py의 부모노드를 px로 변경
    else: #아니면
        parent[py] += parent[px] #px를 py에 합침
        parent[px] = py #px의 부모노드를 px로 변경

    return True #합칠 수 있음

#크루스칼 
def kruskal(n, edge):
    cost = 0 #비용
    cnt = 0 #횟수
    for u, v, w in edge: #edge에서 u,v,w 가져옴
        if not union(u, v): #합칠 수 없으면
            continue #다음 반복문으로
        
        #합칠 수 있으면
        cost += w #w를 cost에 더하기
        cnt += 1 #cnt 증가

        if cnt == n-1: #n-1회 수행시
            return cost #cost 반환

    return 0 #0 반환

#입력
n, m = map(int, input().split()) #집의 개수, 길의 개수

edge = [tuple(map(int, input().split())) for _ in range(m)] #(A,B,C)

# 초기화
parent = [-1]*(n+1)

edge.sort(key=lambda x:x[2])  # 정렬

# 연산 & 출력
print(kruskal(n-1, edge))