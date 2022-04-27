#BOJ2805 - 나무 자르기
import sys
input=sys.stdin.readline

#자른 나무 길이의 총합을 구하는 함수 
def calc_height(height,cut): #height:나무 길이 리스트, cut:자를 길이
    ans=0
    for h in height:
        if h>=cut: ans+=h-cut
    return ans

#가능한 절단기의 최대 높이 구하는 함수
def find_max(left,right,height,m):
    while left<=right:
        mid=(left+right)//2
        temp=calc_height(height,mid)
        if temp>=m: left=mid+1 #더 자를 수 있으면 
        elif temp<m: right=mid-1 #m보다 작으면 자르는 길이를 짧게 해야함
    return right
     
n,m=map(int,input().split())
height=list(map(int,input().split()))
height.sort()

left=0
right=height[-1]

print(find_max(left,right,height,m))
