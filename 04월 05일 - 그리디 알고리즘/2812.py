import sys
input=sys.stdin.readline

n,k=map(int,input().split())
num=input().rstrip()
stack=[]
#가장 큰 수 n-k개 선택 
for i in range(n):
    #k가 0이 되면 stop
    if k==0 or not stack:
        stack.append(num[i])
        continue
    while stack and k>0:
        if int(stack[-1])<int(num[i]):
            stack.pop()
            k-=1
        else: break
        
    stack.append(num[i])

while k>0:
    stack.pop()
    k-=1

print(''.join(stack))
