import sys
import collections
input=sys.stdin.readline


n=int(input().rstrip()) #N
card=collections.deque() #정렬 후 카드 
a=list(map(int,input().split())) #수열 A

for i in range(n-1,-1,-1):
    x=a[i]
    if x==1:
        card.appendleft(n-i)
    elif x==2:
        #맨위에 넣고 두번째 카드와 swap
        card.appendleft(n-i)
        card[0],card[1]=card[1],card[0]
    else:
        card.append(n-i)
        
print(*card) #원래 카드 배열 출력 


