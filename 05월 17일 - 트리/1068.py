import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) #노드 개수
tree = [[] for _ in range(n)]
line = list(map(int, input().split())) #트리 정보
remove_node = int(input()) #삭제할 노드 번호

#트리 구성하기
for i in range(n):
    if i == remove_node: #삭제할 노드면 넘어가기
        continue
    if line[i] == -1: #루트 노드면 넘어가기
        continue
    tree[line[i]].append(i) #자식 노드에 추가

#삭제할 노드를 시작으로 트리 순회, 삭제했음을 표시
q = deque()
q.append(remove_node) 
while q:
    root = q.popleft()
    #다음 방문할 노드 추가
    for child in tree[root]:
        q.append(child) 
    tree[root] = [-1] #삭제된 노드임을 표시

#리프 노드 개수 구하기
cnt = 0
for t in tree:
    if not t:
        cnt += 1
print(cnt)
