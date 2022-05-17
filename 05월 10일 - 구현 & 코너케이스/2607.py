from collections import *
import sys
input = sys.stdin.readline

#비슷한 단어인지 판단하는 함수
def is_similar(cmp, word):
    cnt = 0 #연산 횟수(더하기, 빼기, 바꾸기)
    word_cnt = defaultdict(int)
    word_cnt.update(Counter(word))
    #비교할 단어보다 짧은 단어면
    if len(cmp) < len(word):
        cnt += len(word)-len(cmp)
    for i in cmp:
        if word_cnt[i] <= 0:
            cnt += 1
        word_cnt[i] -= 1

    return True if cnt < 2 else False 


n = int(input())
word = input().rstrip() #첫 번째 단어
ans = 0 #비슷한 단어 개수

for _ in range(n-1):
    cmp = input().rstrip() #비교할 단어
    if is_similar(cmp, word):
        ans += 1

print(ans)
