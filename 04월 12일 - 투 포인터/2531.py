#BOJ2531 - 회전초밥
import sys
from collections import *
from itertools import *
input=sys.stdin.readline

n,d,k,c=map(int,input().split())
belt=deque(int(input()) for _ in range(n))

max_kind=0 #가장 많은 가짓 수 저장
max_check=set() #가장 많은 가짓수를 가질 때 경우를 저장함
for i in range(n):
    check=set(islice(belt,0,k))
    len_c=len(check)
    belt.rotate(1)

    #c를 먹지 않고 k접시 먹을 때 최대이므로 반복문 종료
    if len_c==k and c not in check: max_check=check; break
    #최대 가짓수 저장
    elif max_kind<len_c:
        max_kind=len_c
        max_check=check
    
max_check.add(c)
print(len(max_check))
