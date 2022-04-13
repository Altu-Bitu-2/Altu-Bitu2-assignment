#BOJ16401 - 과자 나눠주기
import sys
input=sys.stdin.readline

#주어진 길이로 과자를 나눠줄 수 있는지 판단하는 함수
def isPossible_divide(snack,length,m):#m은 사촌 수
    if length==0: return False
    for i in snack: m-=i//length       
    return True if m<=0 else False

#입력
m,n=map(int,input().split())
snack=list(map(int,input().split()))
left,right=0,max(snack) 
ans=0

#나눠줄 수 있는 과자의 최대 길이 구하기
while left<=right:
    mid=(left+right)//2
    if isPossible_divide(snack,mid,m):
        ans=mid
        left=mid+1
    else: right=mid-1

print(ans)
