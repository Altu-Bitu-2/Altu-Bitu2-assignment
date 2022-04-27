#BOJ13422 - 도둑
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m,k=map(int,input().split()) #집의 개수, 연속하는 집 개수, 방범 장치 작동 최소 돈의 양
    houses=list(map(int,input().split()))

    cnt=0 #돈을 훔지는 경우의 수
    sum_h=sum(houses[:m])
    if sum_h<k: cnt+=1
    
    idx=n if n==m else 1 #마을의 모든 집을 털땐 1번만 털어야 함
    while idx<n:
        sum_h+=houses[(idx+m-1)%n]-houses[(idx-1)%n]
        if sum_h<k: cnt+=1
        idx=idx+1
        
    print(cnt)
