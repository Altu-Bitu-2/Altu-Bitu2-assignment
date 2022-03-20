import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
k-=1
people=deque([str(i) for i in range(1,n+1)]) #사람 리스트
yose=list() #요세푸스 순열

print('<', end='')
for i in range(n):
    people.rotate(-k)
    yose.append(people.popleft())

print(', '.join(yose),end='>')
