import sys
input=sys.stdin.readline

t=int(input()) #테스트 케이스 개수

for _ in range(t):
    n=int(input())
    note_one=set(map(int, input().split())) #수첩 1
    
    m=int(input())
    note_two=list(map(int, input().split())) #수첩 2

    #수첩 2가 수첩 1에 있는지 확인
    for i in note_two: 
        if i in note_one:
            print(1)
        else:
            print(0)
 
