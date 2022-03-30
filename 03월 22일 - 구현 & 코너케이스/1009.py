#제곱할 때 반복되는 맨 끝자리 수를 구하는 함수
def repeat_square(n):
    ans=[]
    for i in range(1,10):
        temp=n**i%10
        if  temp not in ans:
            ans.append(temp)
        else:
            return ans

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    a%=10
    
    if a==0:
        print(10)
    else:
        n_square=repeat_square(a)
        b=(b-1)%len(n_square)
        print(n_square[b])
