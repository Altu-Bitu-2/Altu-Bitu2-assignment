#BOJ1484 - 다이어트
import sys
input=sys.stdin.readline

#가능한 현재 몸무게 리스트를 반환하는 함수
def find_weight(g):
    past,present=0,g**0.5
    ans=[]

    #현재 몸무게보다 과거 몸무게가 적게 나가야 함
    while int(present)>past: 
        past+=1
        present=(past**2+g)**0.5
        if present.is_integer():
            ans.append(int(present))
    return ans

g=int(input())
if not find_weight(g): print(-1)
else: print(*find_weight(g),sep='\n')
