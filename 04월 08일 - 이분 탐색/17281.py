#BOJ17281 - 야구
import sys
from itertools import *
input=sys.stdin.readline

#타자 순서를 주면 n이닝 후 점수를 리턴하는 함수
def play_innings(turns):
    global innings
    home_base=0
    turn=0

    for i in innings:
        first_base,second_base,third_base=0,0,0
        out=0
        
        while True:
            if out==3: break #다음 이닝으로
            if i[turns[turn]]==0: out+=1
            #1루타
            elif i[turns[turn]]==1:
                home_base+=third_base
                third_base,second_base,first_base=second_base,first_base,1
            #2루타     
            elif i[turns[turn]]==2:
                home_base+=third_base+second_base
                third_base,second_base,first_base=first_base,1,0
            #3루타   
            elif i[turns[turn]]==3:
                home_base+=third_base+second_base+first_base
                third_base,second_base,first_base=1,0,0
            #홈런
            else:
                home_base+=third_base+second_base+first_base+1
                third_base,second_base,first_base=0,0,0
                
            turn=(turn+1)%9 #다음 타자
    #n이닝 후 얻은 점수 리턴
    return home_base
        
n=int(input())
turns=list(p for p in permutations([i for i in range(9)])if p[3]==0) #4번 타자가 1번 선수인 타순 모두 구하기
innings=[list(map(int,input().split())) for _ in range(n)]
print(max(map(play_innings,turns)))
