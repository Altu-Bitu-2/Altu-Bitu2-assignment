import sys
import collections
input = sys.stdin.readline

n,m=map(int, input().split())
dictionary=collections.defaultdict(int) #단어:나온 횟수

for _ in range(n):
    word=input().rstrip()
    if len(word)>=m:
        dictionary[word]+=1 
          
dict_single=sorted(dictionary.keys(),key=lambda x:(-dictionary[x],-len(x),x)) #단어 빈도, 길이, 사전순 정렬


for i in dict_single:
    print(i)
