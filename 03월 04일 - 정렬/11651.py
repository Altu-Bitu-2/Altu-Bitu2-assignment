n = int(input()) #주어진 점의 개수

data=[] #입력된 데이터
for _ in range(n):
    data.append(tuple(map(int,input().split())))

data.sort(key=lambda x: (x[1], x[0])) #y좌표 x좌표 기준 정렬

for i in data:
    print(i[0],i[1])
