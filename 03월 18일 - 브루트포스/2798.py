import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())
card=list(map(int,input().split()))
card_comb=list(combinations(card,3)) #3장의 카드 선택

max=0
for c in card_comb:
    card_sum=sum(c)
    #m을 넘지 않는 최댓값인지 확인
    if card_sum<=m and card_sum>max:
        max=card_sum
print(max)
