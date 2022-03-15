import sys
import collections
import math
input = sys.stdin.readline


n = int(input())
num_count=collections.defaultdict(int)
num_list=[int(input()) for _ in range(n)]
for i in num_list:
    num_count[i]+=1

num_list.sort(reverse=True)
print(math.floor((sum(num_list)/n)+0.5)) #산술평균
print(num_list[math.floor(n/2+1)-1]) #중앙값

#최빈값
num_set=sorted(num_count.keys(),key=lambda x:(-num_count[x],x)) 
if len(num_set)==1: #원소가 1개면
    print(num_set[0])
elif num_count[num_set[0]]==num_count[num_set[1]]: #최빈값이 여러개면
    print(num_set[1]) #2번째 최빈값 선택
else: #최빈값이 하나면
    print(num_set[0]) #최빈값 출력

print(num_list[0]-num_list[-1]) #범위

