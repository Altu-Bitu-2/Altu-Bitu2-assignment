import sys
import collections
input = sys.stdin.readline

def make_palin(name,n): #name은 딕셔너리, n은 이름 길이
    char_list=sorted(name.items()) #[문자,개수]
    palin_name=''
    odd_count=0

    #이름의 반절 집어넣기
    for i in char_list: 
        palin_name+=i[0]*(int(i[1]/2))     
    palin_half=palin_name[::-1]
    
    for i in char_list: #홀수개인 문자열 추가
        if i[1]%2!=0:
            palin_name+=i[0]
            odd_count+=1
    
    palin_name+=palin_half
    return palin_name, odd_count


eng_name = input().rstrip() #이름
len_name=len(eng_name) #이름 길이
char_count=collections.Counter(eng_name) #{문자열:총개수}


#짝수 길이 문자열: 모든 문자가 짝수개야 함
#홀수 길이 문자열: 하나만 홀수개, 나머지는 모두 짝수개여야 함
name,odd_count=make_palin(char_count,len_name)
if len_name%2!=0: #홀수 길이 이름이면
    if odd_count!=1:
        print("I'm Sorry Hansoo")
    else:
        print(name)
else: #짝수 길이 이름이면
    if odd_count!=0:
        print("I'm Sorry Hansoo")
    else:
        print(name)
