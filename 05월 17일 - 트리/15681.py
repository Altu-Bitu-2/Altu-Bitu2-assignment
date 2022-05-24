from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#특정 노드를 루트로 하는 서브 트리의 노드 개수를 반환하는 함수
def cnt_sub_tree(root):
    #자식 노드가 없으면
    if not tree[root]:
        cnt_node[root] = 1
        return 1

    #이미 노드의 개수를 구했으면
    if cnt_node[root] != 0:
        return cnt_node[root]

    #노드 개수 구하기
    for next in tree[root]:
        cnt_node[root] += cnt_sub_tree(next)
    cnt_node[root] += 1

    return cnt_node[root]

#그래프를 트리로 만드는 함수
def graph_to_tree(root):
    q = deque()
    visited = [False]*(n+1)
    visited[root] = True
    q.append(root)

    while q:  # 큐가 빌때까지
        parent = q.popleft()
        for child in graph[parent]:
            if visited[child]:  # 이미 방문했으면 넘어가기
                continue
            visited[child] = True
            tree[parent].append(child)
            q.append(child)


#입력
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph_to_tree(r)
cnt_node = [0 for _ in range(n+1)]
cnt_sub_tree(r)
#쿼리 입력
for _ in range(q):
    query = int(input())
    print(cnt_node[query])