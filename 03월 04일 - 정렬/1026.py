def s_value(a,b,n): #s값 계산 함수
    s=0
    for i in range(n):
       s+=a[i]*b[i] 
    return s

def b_order(b,n): #b의 크기 순위 리스트를 반환하는 함수
    i=0
    order=[] #[[b],[b의 순위]] 리스트
    arr=[] #b의 순위 리스트

    #[[b],[b의 순위]] 리스트 만들기
    order.append(sorted(list(b),reverse=True))
    order.append([-1]*n)
    #리스트에 순위 집어넣기
    for i in range(n):
        order[1][i]=i
    #order를 b 순서대로 정렬    
    for i in range(n):
        index=order[0].index(b[i])
        arr.append(order[1].pop(index))
        order[0].pop(index)
    
    return arr

n=int(input()) #배열의 길이
a_sorted=[] #정렬된 a
a=list(map(int,input().split()))
b=tuple(map(int,input().split()))
b_order=b_order(b,n) 

#b의 순위에 맞춰 a 정렬
a.sort()
for i in range(n):
    a_sorted.append(a[b_order[i]]) 


print(s_value(a_sorted,b,n))
