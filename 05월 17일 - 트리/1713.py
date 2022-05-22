import sys
input = sys.stdin.readline

n = int(input())  # 사진틀의 개수
k = int(input())  # 추천 횟수
candidate = list(map(int, input().split()))
students = [[0, False] for _ in range(101)]  # [추천 횟수, 게시 여부]
photo = []  # 사진틀

for i in candidate:
    if students[i][1]:  # 사진틀에 이미 게시됐으면
        students[i][0] += 1
        continue

    if len(photo) < n:  # 사진틀이 다 차지 않았으면
        students[i] = [1, True]
        photo.append(i)
        continue

    remove_student = photo[0]  # 삭제할 학생 번호
    min_vote = students[photo[0]][0]  # 최소 추천 수
    for p in photo[1:]:
        if students[p][0] < min_vote:  # 추천 수가 더 작으면
            min_vote = students[p][0]
            remove_student = p

    students[remove_student] = [0, False]  # 삭제된 학생의 추천 수 초기화
    students[i] = [1, True]
    photo.remove(remove_student)
    photo.append(i)

photo.sort()
print(*photo)
