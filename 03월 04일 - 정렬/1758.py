def tip_calc(money,rank): #팁 계산
    tip=money-(rank-1)
    if tip>0:
        return tip
    else: #계산된 팁이 0,음수
        return 0
    

n=int(input()) #사람 수  
tip_list=[int(input()) for _ in range(n)] #tip 리스트

tip_list.sort(reverse=True) #팁 내림차순 정렬
tip_sum=0
for i in range(n): #팁의 합 계산
    tip_sum+=tip_calc(tip_list[i],i+1)
    
print(tip_sum)