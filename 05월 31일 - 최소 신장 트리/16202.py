import sys #sys 모듈
input = sys.stdin.readline #입출력 향상 코드

"""
[MST 게임]

 MST 알고리즘을 여러 번 실행해도 될까?
 1. 크루스칼 알고리즘의 시간 복잡도는 O(ElogE)
    이는 오직 간선을 정렬하는 연산의 시간 복잡도!
    즉, 모든 간선을 한 번 정렬해서 저장해두면 이후 몇 번의 알고리즘을 수행하여도 연산 시간에 큰 영향이 없음
 2. 간선 재사용을 위해 우선순위 큐가 아닌 배열에 저장하고 크루스칼 알고리즘 k번 실행
 3. 매번 크루스칼을 수행할 때마다 제일 먼저 추가한 간선을 제외함
    -> 첫번째 간선은 모든 점이 분리된 상태에서 들어오기 때문에 무조건 사용하게 되어 있고, 이는 사용한 간선 중 가장 짧은 간선
    -> 제외될 간선은 배열의 첫번째 간선부터 순차적 제외
 4. 만약 한 번 MST를 만들 수 없다는게 확인됐다면 이후에도 MST를 만들 수 없음
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
def kruskal(n, m, edge, turn):
    cost = 0 #비용
    cnt = 0 #연결 횟수
    for w in range(turn, m+1):
        u, v = edge[w] #u,v정보를 edge[w]에서 받아옴
        if not union(u, v): #합칠 수 없으면
            continue #다음 반복문으로

        cost += w #w를 cost에 더함
        cnt += 1 #cnt 증가

        if cnt == n-1: #n-1회 반복했으면
            return cost #cost 반환

    return 0 #0 반환

n, m, k = map(int, input().split()) #정점의 수, 간선의 수, 턴 수

edge = [None] + [tuple(map(int, input().split())) for _ in range(m)] #간선 정보

result = [] #결과 리스트

for turn in range(1, k+1): #k번 반복
    # 초기화
    parent = [-1]*(n+1)
    # 연산
    result.append(kruskal(n, m, edge, turn))

    if result[-1] == 0: # 이후의 턴은 모두 0점이므로
        break #반복문 종료

result += [0]*(k-len(result)) #이후 턴들의 점수 저장

# 출력
print(*result)