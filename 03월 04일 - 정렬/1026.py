def s_value(a,b,n): #s값 계산 함수
    s=0
    for i in range(n):
       s+=a[i]*b[i] 
    return s

n=int(input()) #배열의 길이

a=list(map(int,input().split()))
b=list(map(int,input().split()))
 

a.sort()
b.sort(reverse=True)


print(s_value(a,b,n))
