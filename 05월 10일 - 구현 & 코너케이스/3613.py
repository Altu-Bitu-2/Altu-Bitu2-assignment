import sys
input = sys.stdin.readline

#c++ 표기법인지 판단하는 함수
def is_cplus(s):
    if not s.islower():
        return False
    if s[0] == '_' or s[-1] == '_': #변수명이 _로 시작하거나 끝날때
        return False

    #변수명에 '_'가 연속될 때
    prev = s[0]
    for i in s[1:]:
        if prev == '_' and prev == i: 
            return False
        prev = i
    return True

#java 표기법인지 판단하는 함수
def is_java(s):
    #첫번째 문자가 대문자이고 _가 없어야 함
    return not s[0].isupper() and '_' not in s 

#c++ 표기법을 java로 바꾸는 함수
def to_java(s):
    java = s.split(sep='_')
    ans = java[0]
    for j in java[1:]:
        ans += j.capitalize()
    return ans

#java 표기법을 c++로 바꾸는 함수
def to_cplus(s):
    ans = ''
    for i in s:
        if i.isupper():
            ans += '_'
        ans += i.lower()
    return ans

var = input().rstrip()
if is_cplus(var):
    print(to_java(var))
elif is_java(var):
    print(to_cplus(var))
else:
    print('Error!')
