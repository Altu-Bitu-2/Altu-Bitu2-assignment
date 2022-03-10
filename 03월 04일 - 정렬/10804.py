N=10 #구간의 개수
range_sorted=[]
card=[i for i in range(1,21)]

for _ in range(N):
    n,m=map(int, input().split())
    card[n-1:m]=reversed(card[n-1:m])
        
for i in card: 
    print(i,end=' ')
