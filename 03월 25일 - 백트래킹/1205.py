import sys
input=sys.stdin.readline

n,new_score,p=map(int,input().split())
scores=list(map(int,input().split()))

'''새 점수를 랭킹 리스트에 일단 추가한 후 정렬
새 점수가 랭킹 리스트 범위인 p를 넘겨서 정렬되면 -1 출력'''
scores.append(new_score)
scores.sort(reverse=True)

#새 점수가 랭킹 리스트에 올라갈 수 없으면
if scores[-1]==new_score and len(scores)>p:
    print(-1)
else:
    print(scores.index(new_score)+1)
