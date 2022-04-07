import sys #sys 모듈 
import heapq as hq #힙 모듈 
input = sys.stdin.readline #입력 속도 향상

"""
[이중 우선순위 큐]

최대 힙과 최소 힙 두가지로 나누어 저장
다른 힙에서 이미 제거된 값을 판단하기 위해, 큐에 값이 들어올 때마다 is_valid에 상태를 저장한다.
만약 최대 힙/최소 힙에서 값을 꺼냈을 때 해당 인덱스의 is_valid 원소가 False로 표기되어 있다면, 이미 다른 큐를 통해 제거된 값이므로 버리고 다시 꺼내야 한다.
"""

testcase = int(input()) #테스트케이스 개수 입력 받음 

# 힙에서 유효하지 않은 값 삭제하는 함수
def remove_invalid_data(heap):
    # 힙에 데이터가 하나라도 있고, top이 invalid 하면 pop해줌
    while heap and not is_valid[heap[0][1]]: #힙이 비지 않았고 힙의 첫값이 유효하지 않으면 
        hq.heappop(heap) #힙에서 제거
    return #함수 종료

for _ in range(testcase): #테스트케이스만큼 반복
    t = int(input()) #수행할 연산의 수

    max_heap = list() #최대힙
    min_heap = list() #최소힙
    is_valid = list() #유효성 저장 리스트 
    idx = 0     # 이번에 들어올 값의 인덱스
                # is_valid[idx]에 값의 유효성이 저장된다.
    
    for _ in range(t): #연산 수만큼 반복
        cmd, n = input().split() #연산 종류와 연산할 숫자 입력 받음 
        if cmd == 'D': #삭제 연산이면
            if int(n) == 1: #최댓값 삭제 연산
                remove_invalid_data(max_heap) #최대힙에서 삭제
                if max_heap: # 최대힙이 안 비었으면 
                    # 값을 제거한 후에 유효성을 갱신
                    is_valid[hq.heappop(max_heap)[1]] = False #해당값을 제거했음을 표시
            else:#최솟값 삭제 연산
                remove_invalid_data(min_heap) #최소힙에서 삭제
                if min_heap: #최소힙이 안 비었으면 
                    # 값을 제거한 후에 유효성을 갱신
                    is_valid[hq.heappop(min_heap)[1]] = False #해당값을 제거했음을 표시
        else: #삽입 연산이면 
            hq.heappush(max_heap, (-int(n), idx)) #최대힙에 값과 인덱스 push
            hq.heappush(min_heap, (int(n), idx)) #최소힙에 값과 인덱스 push
            is_valid.append(True)   # 우선 유효하다고 저장
            idx += 1 #인덱스 증가 

    # 최종 최솟값과 최댓값을 구하기 전, 유효하지 않은 값이 top에 있으면 제거한다.
    remove_invalid_data(max_heap) #최대힙에서 유효하지 않은 값 제거 
    remove_invalid_data(min_heap) #최소힙에서 유효하지 않은 값 제거

    if max_heap: #힙이 비지 않았으면
        print(-max_heap[0][0], min_heap[0][0]) #최대값, 최솟값 출력
    else: #힙이 비었으면 
        print("EMPTY") #empty 출력
