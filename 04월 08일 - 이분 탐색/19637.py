#BOJ19637 - IF문 좀 대신 써
import sys
from bisect import *
input=sys.stdin.readline

power_list=[]
name_list=[]         

n,m=map(int,input().split())
for _ in range(n):
    #오름차순으로 주어짐
    name,power=input().split()
    name_list.append(name)
    power_list.append(int(power))
    
for _ in range(m):
    #target이 name_list의 어느 idx에 해당하는지 확인
    target=int(input())
    print(name_list[bisect_left(power_list,target)])
