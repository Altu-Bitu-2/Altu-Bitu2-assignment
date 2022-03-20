import sys
from itertools import permutations
input=sys.stdin.readline

def sum_digit(num): #각 자리수 합 구하는 함수
    sum=0
    for i in num:
        sum+=int(i)
    return sum

n=input().rstrip()

if sum_digit(n)%3==0 and '0' in n: #30의 배수면 
    num=sorted(n,reverse=True)
    print(''.join(num))
else:
    print(-1)
