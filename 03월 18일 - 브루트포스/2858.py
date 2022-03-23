def factor(n,r): #n: 총 타일 개수, r: 안쪽 타일 개수
    for i in range(3,int(n**0.5)+1):
        if n%i==0:
            #안쪽 타일의 개수 확인
            if (i-2)*(n/i-2)==r:
                return int(n/i), i
    return -1,-1
            

r,b=map(int,input().split())
print(*factor(r+b,b))
