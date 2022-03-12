import sys
input = sys.stdin.readline

s=input()
s_len=len(s)
s_subset=[] #부분 문자열 리스트

for i in range(1,s_len): #슬라이싱 범위 i 
    for j in range(s_len-i):
        s_subset.append(s[j:j+i])

s_subset=set(s_subset)
print(len(s_subset))
