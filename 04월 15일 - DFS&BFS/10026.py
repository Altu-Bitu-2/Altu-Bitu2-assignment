#BOJ10026 - 적록색약
import sys
import copy
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def solve(x,y,paint):
    if x<0 or x>n-1 or y<0 or y>n-1: #범위 밖이면
        return False

    if paint[x][y]!='' and paint[x][y]==prev: #같은 영역이면
        paint[x][y]='' #방문 표시
        #인접한 부분 방문
        solve(x-1,y,paint)
        solve(x,y-1,paint)
        solve(x+1,y,paint)
        solve(x,y+1,paint)
        return True
    return False

n=int(input())
painting=[list(input().rstrip()) for _ in range(n)]
painting_wk=copy.deepcopy(painting) #색약이 볼때의 그림
for i in range(n):
    for j in range(n):
        if painting_wk[i][j]=='G':
            painting_wk[i][j]='R'

cnt,cnt_wk=0,0 #영역의 개수
for i in range(n):
    for j in range(n):
        
        prev=painting[i][j] #구역의 색 저장
        if solve(i,j,painting):
            cnt+=1
            
        prev=painting_wk[i][j]
        if solve(i,j,painting_wk):
            cnt_wk+=1

print(cnt,cnt_wk)
