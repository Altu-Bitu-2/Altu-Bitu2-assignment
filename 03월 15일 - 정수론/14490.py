import sys
input=sys.stdin.readline

def gcd(a,b):
    if b==0:
        return a
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i    
    return 1


def uclid_gcd(a,b): #유클리드 호제법
    #a>b일 때 a와 b의 최대공약수 리턴
    if b==0:
        return a     
    return gcd(b,a%b)

n,m=map(int,input().rstrip().split(sep=':'))
gcd_num=uclid_gcd(max(n,m),min(n,m)) #최대공약수 구하기

print(n//gcd_num,end=':')
print(m//gcd_num)

