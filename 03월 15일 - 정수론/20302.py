import sys
import collections
input=sys.stdin.readline

MAX=100000
factor=[i for i in range(MAX+1)]

#가장 작은 소인수 구하는 함수
def min_fact(): 
    global factor
    factor=[i for i in range(MAX+1)]
    for i in range(2,MAX+1):
        if factor[i]==i:
            for j in range(2,MAX+1):
                if i*j>MAX:
                    break
                if factor[i*j]==i*j:
                    factor[i*j]=i   
#소인수분해 함수
def factorization(fact,n): 
    global factor
    if n==0:
        fact[n]+=1
        return
    n=abs(n)
    while n>1:
        fact[factor[n]]+=1
        n//=factor[n]

def dessert():
    n=int(input())
    exp=input().split()
    mul=collections.defaultdict(int) #곱셈하는 수의 소인수
    div=collections.defaultdict(int) #나눗셈하는 수의 소인수

    factorization(mul,int(exp[0])) 
    for i in range(1,len(exp)):
        if exp[i]=='*':
            factorization(mul,int(exp[i+1]))
        elif exp[i]=='/':
            factorization(div,int(exp[i+1]))

    if mul.get(0)!=None: #곱하는 수에 0이 있으면
        print('mint chocolate')
        return

    #나눗셈 소인수, 곱셈 소인수 대소 비교
    for i in div.keys(): 
        m=mul.get(i)
        if m==None or m<div[i]: 
            print('toothpaste')
            return
    
    print('mint chocolate') 
    

min_fact() #가장 작은 소인수 구하기
dessert()
