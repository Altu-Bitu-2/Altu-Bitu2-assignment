import sys
input=sys.stdin.readline

def sec_to_clock(c): #초를 h,m,s로 변환 
    h=c//3600%24
    m=c%3600//60%60
    s=c%3600%60%60

    return h,m,s

def clock_to_sec(h,m,s): #h,m,s를 초로 변환
    second=h*3600+m*60+s
    return second

h,m,s = map(int, input().split())
calc=clock_to_sec(h,m,s)

q = int(input()) #쿼리의 개수
for i in range(q):
    data=list(map(int, input().split())) #(T, c)
    if data[0]==1:#T=1
        calc+=data[1]
        
    elif data[0]==2:#T=2
        calc-=data[1]
        
    else:#T=3
        h,m,s=sec_to_clock(calc)
        print(h, m, s)
