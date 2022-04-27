#BOJ1253 - 좋다
import sys
input=sys.stdin.readline

#좋은 
def find_good(idx,arr):
    left,right=0,len(arr)-1
    
    while left<right:
        #자기 자신은 좋은 수에서 제외 
        if left==idx: left+=1; continue
        elif right==idx: right-=1; continue

        temp=num[left]+num[right]
        if temp==num[i]: return 1 #좋은 수이면
        #좋은 수가 아니면
        elif temp<num[i]: left+=1
        else: right-=1
        
    return 0


n=int(input())
num=list(map(int,input().split()))
num.sort()
cnt=0 #좋은 수 개수

for i in range(n):
    cnt+=find_good(i,num)
    
print(cnt)
