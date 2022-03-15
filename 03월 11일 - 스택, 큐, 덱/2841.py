import sys
input = sys.stdin.readline

n,p=map(int,input().split())
count=0 #손가락 움직이는 횟수

guitar={i:[] for i in range(1,7)} #{기타 줄:프랫 스택}

for _ in range(n):
    string,plat=map(int,input().split())
    
    while True:
        if len(guitar[string])==0: #스택이 비었으면
            guitar[string].append(plat)
            count+=1
            
        elif guitar[string][-1]>plat: #손을 떼는 경우 
            del guitar[string][-1]
            count+=1
            
        elif guitar[string][-1]==plat: #이미 누르고 있었던 경우
            break
        
        else: #추가로 프랫 누르는 경우
            guitar[string].append(plat)
            count+=1
        
print(count)
        
