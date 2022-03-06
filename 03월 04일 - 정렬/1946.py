import sys
t=int(input()) #테스트 케이스 개수

for _ in range(t):
    n=int(input()) #지원자 숫자
    data=[]
    for _ in range(n):
        data.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

    data.sort(key=lambda x:x[0]) #1차 점수 기준 정렬
    
    flag=data[0][1] 
    count=0 #탈락자 수
    #2차 점수 비교
    for i in range(1,n): 
        if data[i][1]>flag: #flag보다 등수가 낮으면
            count+=1
        else: #flag보다 더 높은 등수면
            flag=data[i][1] #더 높은 등수로 update
    print(n-count)
