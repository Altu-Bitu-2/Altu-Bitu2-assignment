import sys
input=sys.stdin.readline

n=int(input())
cost=[list(map(int,input().split()))for _ in range(n)]
check=[False for _ in range(n)]
cost_list=set()
path=[0 for i in range(n)] #cost 저장하는 배열

def back(cnt,start,next):
    global cost_list
    if cnt==n:
        temp=[]
        for i in range(cnt):
            temp.append(path[i])
        cost_list.add(tuple(temp))
        return

    for i in range(n):
        if cnt!=n-1 and i==start: #시작도시를 마지막에 방문하는 경우가 아니면
            continue
        elif next==i: #대각선 상의 값이면
            continue
        elif check[i]==False and cost[next][i]!=0:
            check[i]=True
            path[next]=cost[next][i]
            back(cnt+1,start,i)
            check[i]=False

#시작 도시 바꾸면서 방문
for i in range(n):
    back(0,i,i)
print(min(map(sum,cost_list)))
