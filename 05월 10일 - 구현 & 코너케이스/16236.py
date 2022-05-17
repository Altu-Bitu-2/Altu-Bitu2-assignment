import sys #sys 모듈 
from collections import deque #덱 불러오기
input = sys.stdin.readline #입출력 향상

INF = 401 #최대 거리

"""
 [아기 상어]

 1. 상어로부터 가장 가까운 거리에 있는 모든 물고기 탐색 (BFS)
 2. 우선순위 조건에 맞추어 먹으러 갈 물고기 확정
    탐색하는 방향에 우선순위를 두는 걸로 해결되지 않음! (예제 입력 4) 정렬 필요
 3. 상어가 이동할 수 있는 곳이 없을 때까지 BFS 탐색 반복

 입력 범위가 작기 때문에 매번 BFS 탐색을 반복해도 시간 초과 X
 가능한 물고기의 최대 마리 수 : 399마리
 최대 BFS 탐색 횟수 : 399회, 1회 탐색마다 while 문은 최대 400회 미만으로 순회
 총 연산 횟수 약 160000번으로 충분히 가능

 해설 : https://myunji.tistory.com/378
 *글 자체는 별로 도움이 안되고...그냥 리팩토링하면 코드가 이렇게 되는구나 정도만 봐주세요
"""

#상어가 이동해야 하는 위치 반환하는 함수
def next_pos(n, shark_size, shark, board):
    #상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    min_dist = INF #물고기의 최소 거리 초기화
    que = deque()   # 상어가 갈 수 있는 곳
    dist = [[0]*n for _ in range(n)]     # 상어로부터의 거리 - 초기값은 0으로
    pos_list = []    # 상어가 먹을 수 있는 물고기들의 위치

    dist[shark[0]][shark[1]] = 1
    que.append(shark)

    while que: #큐가 빌 때까지 반복
        row, col = que.popleft() #큐에서 좌표 가져오기

        # 최단거리 이상은 탐색할 필요 없음
        if dist[row][col] >= min_dist:
            continue

        for i in range(4): #상 하 좌 우 탐색
            nr = row + dr[i] #행 탐색하기 위한 좌표 계산
            nc = col + dc[i] #열 탐색하기 위한 좌표 계산
            if not (0 <= nr < n and 0 <= nc < n) or dist[nr][nc] or board[nr][nc] > shark_size: #범위 밖, 빈칸이거나 상어 크기가 물고기 크기보다 작으면 탐색하지 않음
                continue

            dist[nr][nc] = dist[row][col] + 1 #거리 갱신
            
            # 먹을 수 있는 물고기 발견
            if board[nr][nc] and board[nr][nc] < shark_size: #빈칸이 아니고 먹을 수 있는 물고기면
                pos_list.append((nr, nc)) #물고기 위치 저장
                min_dist = dist[nr][nc] #최소 거리 갱신
                continue
            
            que.append((nr, nc)) #큐에 다음에 방문할 좌표 추가 

    # 상어가 갈 수 있는 곳이 없음
    if not pos_list:
        return min_dist, (-1, -1)

    pos_list.sort() #좌표 정렬하기

    return min_dist - 1, pos_list[0]

#상어가 가능한 모든 물고기를 잡아먹는 데 걸리는 시간 반환하는 함수
def simulation(n, shark, board):
    ans = cnt = 0 #물고기 잡아먹을 수 있는 시간, 잡아먹은 물고기 수
    size = 2 #상어 크기

    while True: #무한 루프
        dist, pos = next_pos(n, size, shark, board) #상어가 가야할 다음 위치, 그 위치까지의 거리 계산
        # 더 이상 먹을 수 있는 물고기가 공간에 없음
        if dist == INF:
            break
        
        ans += dist #물고기 먹는 데 걸린 시간 더함
        cnt += 1 #잡아먹은 물고기 수 증가
        
        # 상어 크기 증가
        if cnt == size:
            cnt = 0 #잡아먹은 물고기 수 초기화
            size += 1 #크기 증가

        # 상어 이동
        board[shark[0]][shark[1]] = 0 #빈칸이 되었으므로 표시
        shark = pos #상어 위치 이동

    return ans #물고기 잡아먹는 시간 반환

# 입력
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n): #i번 반복
    for j in range(n): #j번 반복
        if board[i][j] == 9: #상어의 시작 위치가 나오면
            shark_pos = (i, j) #좌표 저장
            break

print(simulation(n, shark_pos, board)) #결과 출력