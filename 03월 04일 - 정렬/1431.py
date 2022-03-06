def sum_string(str): #시리얼 내 숫자 계산
    sum=0
    for i in range(len(str)):
        if str[i].isdigit(): #숫자만 계산
            sum+=int(str[i])
    return sum

n = int(input())#기타의 개수
data=[]
for _ in range(n):
    data.append(input())

data.sort() #사전순 정렬
data.sort(key=lambda x:(len(x),sum_string(x))) #시리얼 내 숫자 기준 정렬
for i in data:
    print(i)
