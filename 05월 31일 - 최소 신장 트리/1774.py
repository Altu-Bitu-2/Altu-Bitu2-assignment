import sys #sys 모듈
input = sys.stdin.readline #입출력 향상 코드

"""
[우주신과의 교감]

4386번 : 별자리 만들기의 응용 문제
 이미 연결된 정점들이 존재한다는 것을 제외하고는 4386번과 동일

 1. 임의의 두 별에 대한 거리(간선) 모두 구하기
 2. 이미 존재하는 통로들 표시
    !주의! 통로의 개수가 m개라면 v-m-1개의 간선만 더 추가하면 될까?
          이미 연결된 통로들도 사이클을 이룰 수 있기 때문에 유니온 연산을 하며 사이클 없이 연결된 간선만 세기
 3. 이미 연결된 통로의 수를 k개라고 하면 v-k-1개의 간선을 추가로 선택
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

# 입력
n, m = map(int, input().split()) #우주신 개수, 통로 개수
position = [tuple(map(int, input().split())) for _ in range(n)] #좌표
edge = [] #통로의 길이 저장하는 리스트

for i in range(n): 
    for j in range(i): 
        dx = position[i][0] - position[j][0] #x좌표 차이 계산
        dy = position[i][1] - position[j][1] #y좌표 차이 계산

        edge.append((i, j, (dx**2 + dy**2)**(1/2))) #통로 쌍과 길이 edge에 저장

# 초기화
parent = [-1]*(n)

cnt = 0 #연결 횟수 

for _ in range(m): #이미 연결된 통로 정보
    u, v = map(int, input().split()) #입력 받음
    # 이미 연결한 통로
    if union(u-1, v-1): #연결할 수 있으면
        cnt += 1 #cnt 증가

edge.sort(key=lambda x:x[2])  # 정렬

# 연산 & 출력
print("%.2f" %(kruskal(n - cnt, edge)))