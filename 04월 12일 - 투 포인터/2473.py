#BOJ2473 - 세 용액 
import sys
input=sys.stdin.readline

#합이 0에 가장 가까운 세 용액 찾는 함수
def find_mix(n,liquid):
    min_diff=3e9+1
    ans=[]
    
    for i in range(n-2):
        left,right=i+1,n-1
        while left<right:

            mix=liquid[i]+liquid[left]+liquid[right]
            
            if mix==0: return [liquid[i],liquid[left],liquid[right]]
            
            #합이 0이 아니면 0에 가장 가깝도록 함
            if abs(mix)<min_diff: 
                min_diff=abs(mix)
                ans=[liquid[i],liquid[left],liquid[right]]
                
            if mix<0:left+=1
            else:right-=1
          
    return ans
    
n=int(input())
liquid=list(map(int,input().split()))
liquid.sort()
print(*find_mix(n,liquid))
