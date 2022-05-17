import sys
from collections import deque
input = sys.stdin.readline
N = 19

#탐색할 범위 선택하는 함수
def dxy(x, y, mode):
    #상하, 좌우, 좌상향, 우상향
    temp = [((x+1, y), (x-1, y)), ((x, y-1), (x, y+1)),
            ((x-1, y-1), (x+1, y+1)), ((x-1, y+1), (x+1, y-1))]
    return temp[mode]

#주어진 범위 내에서 탐색하는 함수
def sub_solve(i, j, mode):
    temp = []
    q = deque()
    q.appendleft((i, j))
    check = set()
    check.add((i, j))

    while q:
        x, y = q.popleft()
        temp.append((x, y))
        for nx, ny in dxy(x, y, mode):
            if not (0 <= nx < N and 0 <= ny < N): #범위를 벗어나면
                continue
            if board[nx][ny] != board[i][j]: #같은 색 바둑돌이 아니면
                continue
            if (nx, ny) not in check: #이미 확인한 바둑돌인지 체크
                q.append((nx, ny))
                check.add((nx, ny))
    return temp

#상하, 좌우, 우상향 대각, 좌상향 대각 각각에 대해 바둑돌이 5개인지 확인
def solve(i, j):
    for mode in range(4):
        ans = sub_solve(i, j, mode)
        if len(ans) == 5:
            return ans
    return []


board = [list(map(int, input().split())) for _ in range(N)]
flag = False #승부가 났는지 체크하는 플래그
for i in range(N):
    if flag:
        break
    for j in range(N):
        #빈 바둑판은 넘김
        if board[i][j] == 0: 
            continue
        temp = solve(i, j)
        if temp: #바둑돌 5개가 완성됐으면
            print(board[i][j]) #바둑돌 번호 출력
            flag = True
            break
if flag: #승부가 났으면
    temp.sort(key=lambda x: (x[1], x[0])) #가장 왼쪽, 가장 위쪽인 좌표 구하기 위해 정렬
    print(temp[0][0]+1, temp[0][1]+1)
else: #아직 승부가 안 났음
    print(0)