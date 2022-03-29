import sys
from itertools import combinations
input=sys.stdin.readline

#모음인지 확인하는 함수
def is_vowel(char): 
    vowel=['a','e','i','o','u']
    if char in vowel:
        return True
    else:
        return False

l,c=map(int,input().split())
char=list(input().rstrip().split())
vowels=[] #모음
conson=[] #자음
for i in char:
    #모음, 자음 구분
    if is_vowel(i):
        vowels.append(i)
    else:
        conson.append(i)

ans=[]
for i in range(1,l-1):
    #모음, 자음 조합 합치기
    v_c=list(combinations(vowels,i))
    c_c=list(combinations(conson,l-i))
    ans+=[''.join(sorted(vc+cc)) for vc in v_c for cc in c_c]

ans.sort()
for i in ans:
    print(i)
