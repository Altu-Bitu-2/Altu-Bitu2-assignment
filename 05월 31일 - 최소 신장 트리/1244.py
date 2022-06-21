import sys #sys 모듈
input = sys.stdin.readline #입출력 향상 코드

"""
[스위치 켜고 끄기]

 남학생 -> 해당 번호의 배수에 해당하는 스위치 상태 바꾸기
 여학생 -> 해당 번호를 중심으로 좌우 대칭이면서 가장 많은 스위치 포함하는 구간의 상태 모두 바꾸기

 좌우 대칭 검사 시, 스위치 범위 주의 (주어진 스위치 범위 넘어가지 않도록)
 스위치 20개씩 출력하는 부분 주의
 인덱스 번호 주의
"""

# 남학생의 스위치 바꾸기
def change_switch_boy(k, n, switch):
    # k-1 부터 -> 인덱스는 0부터니까
    for i in range(k-1, n, k): #k의 배수 스위치
        switch[i] = 1 - switch[i] #스위치 상태 바꾸기
    return

# 여학생의 스위치 바꾸기
def change_switch_girl(k, n, switch):
    k -= 1  # 인덱스는 0부터
    idx = 0 # 대칭 구간
    # 스위치 범위가 넘어가거나 좌우 대칭이 깨질 때가지
    while k-idx >= 0 and k+idx < n and switch[k-idx] == switch[k+idx]: #스위치 범위 안이고 스위치가 대칭이면
        switch[k-idx] = switch[k+idx] = 1 - switch[k+idx] #스위치 상태 바꾸기
        idx += 1 #다음 대칭으로
    return

# 입력
n = int(input()) #스위치 개수
switch = list(map(int, input().split())) #스위치 정보 
k = int(input()) #성별 정보 개수

for _ in range(k): #k번 반복
    a, b = map(int, input().split()) #성별, 스위치 번호
    if a == 1: #남자면
        change_switch_boy(b, n, switch) #남학생의 스위치 바꾸기
    else: #여자면
        change_switch_girl(b, n, switch) #여학생의 스위치 바꾸기

# 출력
for i in range(0, n, 20): #스위치 20개 단위로 
    print(*switch[i:i+20]) #출력하기