N=10 #구간의 개수
range_sorted=[]
card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(N):
    n,m=map(int, input().split())
    for i in range(n-1,m): #역배치할 구간의 리스트
        range_sorted.append(card[i])
    for j in range(n-1,m): #역배치한 원소 집어넣기
        card[j]=range_sorted.pop(-1)
    
        
for i in range(len(card)):  
    print(card[i],end=' ')
