#BOJ2840 - 행운의 바퀴
import sys
from collections import *
input=sys.stdin.readline

def main():
    n,k=map(int,input().split())
    roulette=['?']*n
    check=set()
    arrow=0
    for _ in range(k):
        times,alpha=input().rstrip().split()
        arrow=(arrow-int(times))%n #화살표 위치 

        #해당하는 행운의 바퀴가 없는 경우
        if roulette[arrow]!=alpha and roulette[arrow]!='?': #다른 문자가 들어있는 룰렛에 문자를 집어넣을 경우
            print('!')
            return
        
        if roulette[arrow]=='?' and alpha in check: #넣을 문자가 이미 다른 룰렛의 칸에 들어가 있는 문자일 경우
            print('!')
            return
        
        roulette[arrow]=alpha
        check.add(alpha)

    
    print(''.join(roulette[arrow:]+roulette[:arrow]))
main()
