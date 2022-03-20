import sys
input=sys.stdin.readline

prior={'(':5,')':0,'+':3,'-':3,'*':1,'/':1} #스택에서 연산자 우선순위

def is_empty(stack):
    return len(stack)==0
def is_operator(char): 
    return char in '+*-/()'

postfix='' #표현식
operator=[]
infix=input().rstrip()

for char in infix:
    #피연산자
    if is_operator(char)!=True:
        postfix+=char
        continue
    #연산자 연산
    elif char=='(': #열린 괄호
        operator.append(char)
        continue
    
    elif char==')': #닫힌 괄호
        while is_empty(operator)!=True: #열린 괄호가 나올때까지 pop
            opp=operator.pop()
            if opp=='(':
                break
            postfix+=opp
            
    #사칙연산자       
    elif is_empty(operator): 
        operator.append(char)
    else:
        while is_empty(operator)!=True:
            if prior[operator[-1]]<=prior[char]: #우선순위가 더 큰 연산자가 들어왔으면
                postfix+=operator.pop()
            else:
                break
        
        operator.append(char)

#스택 비우기
while is_empty(operator)!=True:  
    postfix+=operator.pop()
    
print(postfix)
