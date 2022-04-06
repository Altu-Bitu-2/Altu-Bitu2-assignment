import sys
from itertools import chain
from collections import deque
input=sys.stdin.readline

l=int(input())
for _ in range(l):
    prev_cursor=deque() #커서 전 문자열을 담음 
    next_cursor=deque() #커서 후 문자열을 담음
    line=input().rstrip()
    for i in line:
        if i=='<':
            if prev_cursor:
                next_cursor.appendleft(prev_cursor.pop())
        elif i=='>':
            if next_cursor:
                prev_cursor.append(next_cursor.popleft())
        elif i=='-':
            if prev_cursor:
                prev_cursor.pop()
        else:
            prev_cursor.append(i)

    print(''.join(chain(prev_cursor,next_cursor)))
