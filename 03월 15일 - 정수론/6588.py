import sys
import math
input=sys.stdin.readline
#sys.stdin=open('input.txt','r')
#lines=sys.stdin.readlines()

def is_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True

def goldbach(n):
    flag=False
    for i in range(3,n//2+1,2):
        if is_prime(i) and is_prime(n-i):
            print(f'{n} = {i} + {n-i}')
            flag=True
            break
        
    if flag!=True:
        print('Goldbach\'s conjecture is wrong.')

while True: 
    n=int(input())
    if n==0:
        break        
    goldbach(n)
