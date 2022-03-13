import sys
input = sys.stdin.readline

def calc_case(case): #의상을 입을 수 있는 경우의 수 계산
    num = 1
    for i in case.values():
        num *= i+1
    return num-1
    
    
t = int(input()) #테스트 케이스 개수
fashion = {}

for i in range(t):
    fashion.clear()
    n = int(input()) #해빈이가 가진 의상 수
    for i in range(n):
        costume, cst_type = input().split()
        if cst_type in fashion:
            fashion[cst_type]+=1
        else:
            fashion[cst_type] = 1
            
    print(calc_case(fashion))
         
