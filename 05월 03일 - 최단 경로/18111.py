import sys
input=sys.stdin.readline

#땅고르기에 필요한 시간을 리턴하는 함수 
def make_flat(h,ground):
    #h는 만들고자 하는 땅의 높이
    cnt_dig=0
    cnt_build=0
    
    for row in ground:
        for col in row:
            if col>h: #기준 높이보다 높으면 깎기
                cnt_dig+=col-h
            elif col<h: #낮으면 쌓기 
                cnt_build+=h-col

    #블록이 필요한 개수만큼 없으면 -1 반환, 있으면 땅고르기 하는 데 걸리는 시간 반환
    return cnt_dig*2+cnt_build if b+cnt_dig>=cnt_build else -1        

n,m,b=map(int,input().split())
ground=[list(map(int,input().split())) for _ in range(n)]
max_height=max(map(max,ground))
min_time=500*500*256*2+1 #땅고르기 하는 데 걸리는 시간
ans=max_height #땅의 높이

for h in range(max_height,-1,-1):
    time=make_flat(h,ground)
    #h 높이로 땅고르기가 불가능하면
    if time==-1:
        continue
    
    if time<min_time:
        ans=h
        min_time=time

print(min_time,ans)