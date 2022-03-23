a,b=map(list,input().split())
#일의 자리가 index 0이 되도록
a=list(map(int,a))[::-1]
b=list(map(int,b))[::-1]

min_len=min(len(a),len(b))
ans=[]
carry=0 #받아올림 

#길이가 짧은 수까지 덧셈
for i in range(0,min_len):
    sum_ab=a[i]+b[i]+carry
    if sum_ab>=10:
        ans.append(sum_ab%10)
        carry=1
    else:
        ans.append(sum_ab)
        carry=0
        
#나머지 자릿수 덧셈
if len(a)>len(b):
    for i in range(len(b),len(a)):
        ans.append(a[i])
    ans[len(b)]+=carry
    #받아올림 있는지 확인
    for i in range(len(b),len(a)-1):
        if ans[i]>=10:
            ans[i]%=10
            ans[i+1]+=1   

elif len(a)<len(b):
    for i in range(len(a),len(b)):
        ans.append(b[i])
    ans[len(a)]+=carry
    #받아올림 있는지 확인
    for i in range(len(a),len(b)-1):
        if ans[i]>=10:
            ans[i]%=10
            ans[i+1]+=1
#자릿수가 같으면
else:
    if carry!=0:
        ans.append(carry)

for i in ans[::-1]:
    print(i,end='')

