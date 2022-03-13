import sys
import collections
input = sys.stdin.readline

n=int(input())
ext_list=collections.defaultdict(int) #확장자:나온 횟수 딕셔너리
for _ in range(n):
    ext=list(input().rstrip().split(sep='.'))[-1] #확장자 추출
    ext_list[ext]=ext_list[ext]+1


for i in sorted(ext_list):
    print(i,ext_list[i])
