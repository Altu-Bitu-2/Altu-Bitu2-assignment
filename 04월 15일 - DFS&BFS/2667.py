#BOJ2667 - 단지번호붙이기
import sys
input=sys.stdin.readline

def solve(x,y):
    global cnt
    if x<0 or x>n-1 or y<0 or y>n-1: #범위 밖이면
        return False
    #아직 방문하지 않았으면
    if houses[x][y]==1: 
        cnt+=1
        houses[x][y]=0
        #인접한 집 방문
        solve(x-1,y)
        solve(x,y-1)
        solve(x+1,y)
        solve(x,y+1)
        return True
    return False
        
n=int(input())
houses=[list(map(int,input().rstrip())) for _ in range(n)]
ans=[] #단지 내 집의 개수 저장하는 리스트
result,cnt=0,0 #단지의 개수, 단지 내 집의 개수
for i in range(n):
    for j in range(n):
        if solve(i,j):
            ans.append(cnt)
            result+=1
            cnt=0
            
print(result) 
ans.sort() #오름차순 정렬
print(*ans,sep='\n')
