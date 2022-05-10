import sys #sys 모듈
from collections import deque #deque 가져오기
input = sys.stdin.readline #입출력 속도 향상

"""
[Puyo Puyo] - bfs, 시뮬레이션 문제

1. bfs 탐색을 통해 4개 이상의 뿌요가 모였는지 확인
2. 4개 이상의 뿌요가 모였다면, 해당되는 영역을 '.'으로 바꾸어 비워줌
3. 전체 필드에 대해 1~2를 다 수행한 후, 뿌요를 떨어뜨림
    - 바닥부터 시작해서 남아있는 뿌요들을 모으고, 남은 부분은 '.'으로 채우는 방식
4. 터뜨릴 수 없을 때까지 반복

여기서, 3번 과정을 편하게 하기 위해 12*6으로 들어오는 입력을 6*12로 바꾸어준다.
같은 열에 있는 데이터를 다루는 것보다 같은 행에 있는 데이터를 다루는 것이 편하기 때문이다.
"""

# 행과 열을 바꾸어 사용하므로 ROW를 6, COL은 12로 설정
ROW = 6
COL = 12

#(i,j)를 시작 지점으로 bfs 탐색하는 함수
def bfs(i, j): 
    dr = [-1, +1, 0, 0] #탐색 시 row 이동 방향
    dc = [0, 0, -1, +1] #탐색 시 col 이동 방향 
    que = deque() #큐 선언
    
    que.append((i, j)) #큐에 (i,j) 삽입
    visited = [[False]*COL for _ in range(ROW)] #탐색 여부 저장하는 배열 선언
    visited[i][j] = True #(i,j) 탐색 확인
    color = board[i][j] #(i,j)의 색 
    count = 1   # 모여있는 뿌요의 개수
    cords = []  # 포함된 좌표 저장할 리스트

    while que: #큐가 빌 때까지
        cords.append(que[0]) #같은 색인 뿌요 좌표 저장
        r, c = que.popleft() #row, col값 받기
        for x in range(4): #상하좌우 탐색
            nr, nc = r+dr[x], c+dc[x]
            if not (0 <= nr < ROW and 0 <= nc < COL): #보드 범위를 벗어나면
                continue #다음 반복문으로
            if not visited[nr][nc] and board[nr][nc] == color: #탐색하지 않았고 같은 색 뿌요면
                visited[nr][nc] = True #탐색 확인
                que.append((nr, nc)) #큐에 좌표 삽입
                count += 1 #뿌요 개수 체크
    
    if count < 4: #모여있는 뿌요가 4개보다 작으면
        return False #True 반환

    #모여있는 뿌요가 4개 이상이면
    for r, c in cords: #cords에 저장된 좌표 꺼내기
        board[r][c] = '.' #(r,c)에 있는 뿌요 터트리기

    return True #True 반환

# 뿌요를 터뜨린 이후의 새 필드를 작성하는 함수
def make_new_board(board):
    new_board = [] #새 필드 선언
    for i in range(ROW): #ROW만큼 반복
        temp = [] #임시 리스트 선언
        for j in range(COL): #COL만큼 반복
            # 남아있는 뿌요를 임시 리스트에 모으기
            if board[i][j] != '.': #아래로 내려야 하는 뿌요이면
                temp.append(board[i][j]) #뿌요 모으기
        # 비어 있는 부분을 '.'로 채우기
        while len(temp) < COL: #temp가 덜 채워졌으면
            temp.append('.') #. 채우기
        new_board.append(temp[:]) #새 필드에 temp 추가
    return new_board #새 필드 반환

# 입력
board = [[None]*COL for _ in range(ROW)]

# 행과 열을 바꾸어 저장
for i in range(COL): #COL만큼 반복
    line = input().rstrip() #입력받은 줄
    for j in range(ROW): #ROW만큼 반복
        board[j][12-i-1] = line[j] #입력된 값을 행과 열 바꾸어서 저장
        
ans = 0 #연쇄 회수

while True: #무한 루프
    flag = False #연쇄가 발생했는지 확인
    for i in range(ROW): #ROW 만큼 반복
        for j in range(COL): #COL만큼 반복
            if board[i][j] == '.': #비어있는 칸이면
                continue #다음 반복문으로 
            if bfs(i, j): #뿌요가 있는 칸이고 연쇄가 발생하면
                flag = True #flag를 True로 만듦
    
    if not flag: #flag가 False면
        break #무한 루프 종료
    ans += 1 #flag가 True면, 연쇄 회수 늘려줌
    board = make_new_board(board) #연쇄 후 필드를 업데이트

print(ans) #연쇄 회수 출력