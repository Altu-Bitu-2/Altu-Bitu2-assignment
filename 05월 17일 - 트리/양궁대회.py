SIZE = 10 #과녁 크기 선언

"""
 [양궁대회]

 1. 가능한 모든 경우를 백트래킹 탐색을 통해 검사
 -> 라이언이 점수를 얻어가려면 어피치보다 1개 더 쏘는 경우가 최적. 어피치보다 적게 화살 쏘는 건 점수 못 얻어가므로 어차피 의미가 없음.
 -> 따라서 라이언이 각 점수에 화살을 아래와 같이 쏘는 2가지 경우만 고려해서 만들어지는 모든 경우를 백트래킹으로 탐색
    - 어피치가 점수 획득을 하는 경우: 해당 점수에는 화살을 한 발도 쏘지 않는 것이 이득
    - 라이언이 점수 획득을 하는 경우: 필요한 최소 화살을 사용하는 것이 이득이므로 어피치보다 정확히 한 발 더 쏨

 !주의! 0번 인덱스가 10점 과녁임을 주의
"""

max_diff = 1 #점수 차 변수
answer = [-1] #정답 배열

#백트래킹 수행하는 함수
def backtracking(idx, left, diff, ryan, appeach):
    global max_diff, answer
    # 기저조건 - 0점 과녁까지 모두 탐색한 경우
    if idx == SIZE: #0번 과녁까지 탐색 했으면
        ryan[idx] = left #남은 점수 모두 대입
        
        if diff > max_diff: #더 큰 점수차면
            max_diff = diff #diff를 max_diff로 
            answer = ryan[:] #ryan 배열을 정답 배열에 대입 
        elif diff == max_diff: #diff가 max_diff와 동일하면
            if ryan[::-1] > answer[::-1]: #작은 점수 쏜 횟수가 많으면
                answer = ryan[:] #정답 배열 ryan으로 바꿈
        return #종료
    
    # 남은 화살로 라이언이 점수를 얻을 수 있는 경우
    if left > appeach[idx]:
        ryan[idx] = appeach[idx] + 1 #어피치보다 더 많은 화살을 쏨
        backtracking(idx+1, left - ryan[idx], diff + SIZE - idx, ryan, appeach) #백트래킹 실행
        ryan[idx] = 0 #백트래킹 실행 후 ryan 점수 되돌리기 

    # 어피치가 점수를 얻을 수 있는 경우 점수 계산
    if appeach[idx]: 
        diff -= SIZE - idx #점수 차 계산
    backtracking(idx+1, left, diff, ryan, appeach) #백트래킹 실행
    return #종료

def solution(n, info):
    ryan = [0]*11   # 라이언 과녁 정보
    backtracking(0, n, 0, ryan, info) #백트래킹 실행
    
    return answer #정답 반환


# 디버깅 위한 메인 코드 - 프로그래머스에는 제출 X
if __name__ == "__main__":
    n = 5 #화살 수
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0] #어피치 화살 정보

    print(*solution(n, info)) #정답 출력