def tip(money,rank): #팁 계산
    tip=money-(rank-1)
    if tip>0:
        return tip
    else: #계산된 팁이 0,음수
        return 0
    

n=int(input()) #사람 수  
tip_list=[] #tip 리스트
for i in range(n):
    tip_list.append(int(input()))

tip_list.sort(reverse=True) #팁 내림차순 정렬
tip_sum=0
for i in range(len(tip_list)): #팁의 합 계산
    tip_sum+=tip(tip_list[i],i+1)
    
print(tip_sum)

