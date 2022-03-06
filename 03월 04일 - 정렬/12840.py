def sec_to_clock(c): #초를 h,m,s로 변환 
    if c>0:#초가 양수일때
        h=c//3600%24
        m=c%3600//60%60
        s=c%3600%60%60
    else: #초가 음수일때
        h=24-(abs(c)//3600%24)
        m=60-(abs(c)%3600//60%60)
        s=60-(abs(c)%3600%60%60)
        if s!=60:
            h-=1
            m-=1
        elif m!=60:
            h-=1
    h%=24
    m%=60
    s%=60  
    return h,m,s

def clock_to_sec(h,m,s): #h,m,s를 초로 변환
    second=h*3600+m*60+s
    return second


h,m,s = map(int, input().split())


q = int(input()) #쿼리의 개수
for i in range(q):
    data=list(map(int, input().split())) #(T, c)
    if data[0]==1:#T=1
        calc=clock_to_sec(h,m,s)+data[1]
        h,m,s=sec_to_clock(calc)
        
    elif data[0]==2:#T=2
        calc=clock_to_sec(h,m,s)-data[1]
        h,m,s=sec_to_clock(calc)
        
    else:#T=3
        print(h, m, s)
