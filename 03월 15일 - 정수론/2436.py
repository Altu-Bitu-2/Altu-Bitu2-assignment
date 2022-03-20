import sys
input=sys.stdin.readline

#n의 약수 절반을 구하는 함수
def factorization(n): 
    fact=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
          fact.append(i)
    return fact

def gcd(a,b): #a>b
    if b==0:
        return a
    
    for i in range(b,0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1


def uclid_gcd(a,b): #a>b
    if b==0:
        return a
    return gcd(b,a%b)


g,l=map(int,input().split())
div=l/g
min=g*l+2
min_list=[]
factor=factorization(div)

for i in range(len(factor)):
    a,b=g*factor[i],g*(int(div/factor[i]))
    if uclid_gcd(b,a)!=g: 
        continue
    if min>a+b: #a,b의 최대공약수가 g일 때
        min_list=[a,b]
        min=sum(min_list)
        
print(*min_list)

