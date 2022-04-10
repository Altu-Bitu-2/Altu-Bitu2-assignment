import sys
input=sys.stdin.readline

n=int(input())
road=list(map(int,input().split()))
gas=list(map(int,input().split()))[:-1]
#지역 도착하기 전까지 최소 주유소 구하기
min_gas=gas[0]
for i in range(1,n-1):
    if min_gas>gas[i]:
        min_gas=gas[i]
    elif min_gas<gas[i]:
        gas[i]=min_gas
#비용 계산
print(sum(map(lambda x,y:x*y,gas,road)))

