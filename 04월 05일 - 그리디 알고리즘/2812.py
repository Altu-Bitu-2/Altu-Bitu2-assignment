import sys
input=sys.stdin.readline

n,k=map(int,input().split())
cnt=k
num=input().rstrip()
stack=[]
#가장 큰 수 n-k개 선택 
for i in num:
    #k가 0이 되면 stop
    if cnt==0 or not stack:
        stack.append(i)
        continue
    while stack and cnt>0 and int(stack[-1])<int(i):
        stack.pop()
        cnt-=1
    stack.append(i)

print(''.join(stack[:n-k]))
