import sys
input=sys.stdin.readline

n,k=map(int,input().split())
k-=1
people=[i for i in range(1,n+1)] #사람 리스트
yose=list() #요세푸스 순열
index=0 #people에서 첫번째 사람을 가리킴

print('<', end='')
for i in range(n):
    if index>n-i: #index가 리스트에 남은 사람 수보다 크면
        index=0
    index=(index+k)%(n-i) #k번째 사람의 위치
    if i==n-1: #마지막 사람 출력시 
       print(people.pop(index),end='')
    else:
        print(people.pop(index),end=', ')

print('>')

  
