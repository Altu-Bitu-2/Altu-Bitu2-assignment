#BOJ16234 - 인구이동
import sys
sys.setrecursionlimit(10**5) 
import copy
from collections import *
input=sys.stdin.readline

#(x,y)가 범위 내에 있는지 확인하는 함수
def is_range(x,y):
    return 0<=x<=n-1 and 0<=y<=n-1

#nation[x][y]를 반환하는 함수
def map_list(idx):
    return nations[idx[0]][idx[1]]

def solve(x,y):
    global ans
    if not is_range(x,y):
        return False

    #방문하지 않았으면
    if not check[x][y]:
        check[x][y]=True
        ans.append((x,y))
        for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)): #인접 국가 순회
            if is_range(nx,ny) and l<=abs(nations[x][y]-nations[nx][ny])<=r:
                solve(nx,ny)
        return True
    return False
    
n,l,r=map(int,input().split())#인구 차이 l명 이상 r명이하 
nations=[list(map(int,input().split())) for _ in range(n)]
check=[[False for _ in range(n)] for _ in range(n)]
ans,temp=[],[]
cnt=0

while True:
    temp=[]
    for i in range(n):
        for j in range(n):
            #같은 구역의 국가끼리 ans로 묶어줌
            if solve(i,j):
                temp.append(ans)
                ans=[]
                
    if  len(temp)==n*n: break #인구이동이 일어나지 않으면 종료

    #인구이동
    for t in temp:
        result=sum(map(map_list,t))//len(t)
        for x,y in t:
            nations[x][y]=result
            check[x][y]=False
    cnt+=1
print(cnt)
