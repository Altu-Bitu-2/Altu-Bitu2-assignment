import sys
input=sys.stdin.readline

blackboard=[] #검은색으로 시작하는 8*8체스판
whiteboard=[] #하얀색으로 시작하는 8*8체스판
for i in range(8):
    if i%2!=0:
        blackboard.append('WBWBWBWB')
    else:
        blackboard.append('BWBWBWBW')
        
for i in range(8):
    if i%2!=0:
        whiteboard.append('BWBWBWBW')
    else:
        whiteboard.append('WBWBWBWB')
    
#8*8체스판 색칠 횟수 구하는 함수
def count_painting(chess):
    cnt_b=0 #검은색으로 처음 칠했을 때
    cnt_w=0 #하얀색으로 처음 칠헸을 때 
    
    for i in range(8):
        for j in range(8):
            if whiteboard[i][j]!=chess[i][j]:
                cnt_w+=1
    for i in range(8):
        for j in range(8):
            if blackboard[i][j]!=chess[i][j]:
                 cnt_b+=1
            
    return min(cnt_w,cnt_b)

    
    
r,c=map(int,input().split())
chessboard=[input().rstrip() for r in range(r)]
min_cnt=r*c
temp=[]
cnt=0
#모든 8*8 체스판 추출
for i in range(r-7):
    for j in range(c-7):
        temp.append([row[j:j+8] for row in chessboard[i:i+8]])

for i in temp:
    cnt=count_painting(i)
    if min_cnt>cnt:
        min_cnt=cnt

print(min_cnt)
    
       


