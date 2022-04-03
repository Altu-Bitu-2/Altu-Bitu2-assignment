import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

dp=[1]*n
for i in range(len(a)):
    for j in range(i+1,n):
        if a[i]<a[j]:
            dp[j]=max(dp[i]+1,dp[j])

print(max(dp))
