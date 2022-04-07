import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
op_num=list(map(int,input().split())) #+-*/ 수
op=[]
exp=['' for _ in range(n-1)]
check=[False for _ in range(n-1)]
exp_list=set()

#연산자 개수 배열을 연산자 배열로 만드는 함수
for i in range(4):
    for j in range(op_num[i]):
        if i==0:
            op.append('+')
        elif i==1:
            op.append('-')
        elif i==2:
            op.append('*')
        else:
            op.append('/')
            
#연산자 배열로 배열 A 계산
def eval_op(op):
    global a
    flag=False
    ans=a[0]
    for i in range(n-1):
        if op[i]=='+':
            ans+=a[i+1]
        elif op[i]=='-':
            ans-=a[i+1]
        elif op[i]=='*':
            ans*=a[i+1]
        elif op[i]=='/':
            if ans<0: #음수 나눗셈
                flag=True
            ans=abs(ans)//a[i+1]
            if flag==True:
                flag=False
                ans=-ans
    return ans
#연산자 배열을 구하는 함수
def back(cnt):
    if cnt==n-1:
        temp=''
        for i in range(cnt):
            temp+=exp[i]
        exp_list.add(temp)
        return

    for i in range(n-1):
        if check[i]==False:
            exp[cnt]=op[i]
            check[i]=True
            back(cnt+1)
            check[i]=False

back(0)
print(max(map(eval_op,exp_list)))
print(min(map(eval_op,exp_list)))