from collections import deque
n,k=map(int,input().split())
import sys
input=sys.stdin.readline
a=deque(map(int,input().split())) #2n까지 존재 내구도
belt=deque(False for _ in range(n)) #벨트 위 로봇이 있는지 저장 

cnt=0
while k>0:
    #1단계
    a.rotate(1) #벨트 회전
    belt.rotate(1)
    #내리는 위치에 오면
    belt[n-1]=False

    #2단계
    for i in range(n-1,-1,-1):
        if belt[i]==True and belt[i+1]==False and a[i+1]>0:
            belt[i],belt[i+1]=False,True
            a[i+1]-=1
            if a[i+1]==0:
                k-=1

    #내리는 위치에 오면
    belt[n-1]=False
            
    #3단계
    if a[0]!=0:
        belt[0]=True
        a[0]-=1
        if a[0]==0:
            k-=1
    cnt+=1
    
print(cnt)
