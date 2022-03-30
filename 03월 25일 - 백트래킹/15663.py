n,m=map(int,input().split())
SIZE=8
num=['' for _ in range(SIZE)]
num_list=sorted(list(input().split()))
check=[False for _ in range(n)]
ans=set()

def back(cnt):
    if cnt==m:
        temp=''
        for i in range(m):
            temp+=num[i]+' '
        ans.add(tuple(map(int,temp.split())))
        return
    
    for i in range(n):
        if check[i]==False:
            check[i]=True
            num[cnt]=num_list[i]
            back(cnt+1)
            check[i]=False

back(0)
ans=sorted(ans)
for i in ans:
    print(*i)