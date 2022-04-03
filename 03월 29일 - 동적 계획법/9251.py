import sys
input=sys.stdin.readline

str1=input().rstrip()
str2=input().rstrip()
row=len(str2)
col=len(str1)

dp=[]
for _ in range(row):
    dp.append([0 for _ in range(col)])

#row=0,col=0인 경우 LCS값 구하기
if str1[0]==str2[0]:
    dp[0][0]=1

for j in range(1,col):
    if str1[j]==str2[0]:
        dp[0][j]=max(dp[0][j-1],dp[0][j]+1)
    else:
        dp[0][j]=dp[0][j-1]

for i in range(1,row):
    if str2[i]==str1[0]:
        dp[i][0]=max(dp[i-1][0],dp[i][0]+1)
    else:
        dp[i][0]=dp[i-1][0]

#나머지 LCS값 구하기
for i in range(1,row):
    for j in range(1,col):
        if str2[i]==str1[j]: #문자열이 같은 경우
            dp[i][j]=dp[i-1][j-1]+1
            
        else: #문자열이 같지 않은 경우
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[row-1][col-1])
        
            
        
