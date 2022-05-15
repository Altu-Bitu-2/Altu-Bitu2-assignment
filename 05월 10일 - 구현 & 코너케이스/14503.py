import sys
from collections import *
input = sys.stdin.readline

#로봇청소기가 청소하는 칸 개수 반환하는 함수
def clean(r, c, direct):
    #서쪽, 동쪽 인덱스 서로 바꿔주기
    if direct == 1:
        direct = 3
    elif direct == 3:
        direct = 1
    #북 서 남 동
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    q = deque()
    q.appendleft((r, c))
    curr_direct = direct
    place[r][c] = 2
    ans = 1

    while q:
        row, col = q.popleft()
        cnt = 0
        while cnt < 4:
            #인접한 칸 탐색
            curr_direct = (curr_direct+1) % 4
            nr, nc = row+dr[curr_direct], col+dc[curr_direct]
            if place[nr][nc] == 0:
                q.append((nr, nc))
                place[nr][nc] = 2
                ans += 1
                break
            cnt += 1

        #후진
        if cnt == 4:
            nr = row-dr[curr_direct]
            nc = col-dc[curr_direct]
            if place[nr][nc] != 1:
                q.append((nr, nc))

    return ans


n, m = map(int, input().split())
r, c, direct = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(n)]
print(clean(r, c, direct))