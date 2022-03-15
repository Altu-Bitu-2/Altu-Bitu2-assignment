import sys
input=sys.stdin.readline

def is_open(bracket):
    return bracket=='(' or bracket=='['

def is_close(bracket):
    return bracket==')' or bracket==']'

def is_empty(stack):
    return len(stack)==0


brackets=input().rstrip()
stack=[] #열린 괄호만 저장하는 스택
exp=''
pointer=-1

for bracket in brackets:
    pointer+=1
    if is_open(bracket):#열린 괄호면
        if pointer>0 and is_close(brackets[pointer-1]): #닫힌 괄호 뒤에 들어왔으면 
            exp+='+'
  
        elif pointer>0 and is_open(brackets[pointer-1]): #열린 괄호가 연속으로 들어왔으면
            exp+='*('
               
        if is_empty(stack): #가장 바깥의 괄호면
            exp+='('
          
        if bracket=='(': 
            exp+='2'
        if bracket=='[':
            exp+='3'
        stack.append(bracket)

        
    else: #닫힌 괄호면
        if is_empty(stack): #짝이 안 맞으면
            print(0)
            sys.exit()
            
        elif stack[-1]=='(' and bracket==')':
            stack.pop()
            if is_empty(stack): #가장 바깥의 괄호면
                exp+=')'
              
            if pointer>0 and is_close(brackets[pointer-1]): #닫힌 괄호가 연속으로 들어왔으면
                exp+=')'
               
                
        elif stack[-1]=='[' and bracket==']':
            stack.pop()
            if is_empty(stack): #가장 바깥의 괄호면
                exp+=')'
                
            if pointer>0 and is_close(brackets[pointer-1]): #닫힌 괄호가 연속으로 들어왔으면
                exp+=')'
               
         
        else: #짝이 안 맞으면
            print(0)
            sys.exit()
            
if is_empty(stack)!=True:
    print(0)
    sys.exit()
        
print(eval(exp))
    

