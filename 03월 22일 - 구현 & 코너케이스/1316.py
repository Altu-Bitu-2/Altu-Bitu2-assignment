#그룹 단어인지 판단하는 함수
def is_group(word):
    point=word[0]
    group=set()
    for i in word:
        #연속되는 문자면
        if i==point: 
            group.add(i)
        #연속되지 않는데 이미 나온 문자면
        elif i in group:
           return False
        #새로 나온 문자면
        else:
            point=i
            group.add(i)
        
    return True
        

n=int(input())
cnt=0
for _ in range(n):
    word=input()
    if is_group(word):
        cnt+=1

print(cnt)
