#BOJ2840 - 행운의 바퀴
import sys
from collections import *
input=sys.stdin.readline


def main():
    n,k=map(int,input().split())
    roulette=deque('?' for i in range(n)) #idx 증가 방향 = 시계방향
    check=set() #룰렛에 이미 들어간 문자인지 확인

    for _ in range(k): #룰렛 정보 주어짐
        times,alpha=input().rstrip().split()
        roulette.rotate(int(times))

        #해당하는 행운의 바퀴가 없는 경우
        if roulette[0]!=alpha and roulette[0]!='?': #다른 문자가 들어있는 룰렛에 문자를 집어넣을 경우
            print('!')
            return
        
        if roulette[0]=='?' and alpha in check: #넣을 문자가 이미 다른 룰렛의 칸에 들어가 있는 문자일 경우
            print('!')
            return
        
        roulette[0]=alpha
        check.add(alpha)

    print(''.join(roulette))

main()
