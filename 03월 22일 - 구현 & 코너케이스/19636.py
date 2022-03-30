import sys
input=sys.stdin.readline
#요요 판단 함수
def is_yoyo(l_0,l,a): #변화한 일일 기초 대사량, 다이어트 전 일일 섭취량, 다이어트 전 활동 대사량
    return l-(l_0+a)>0

#사망 판단 함수
def is_death(w,l_0): #체중, 기초대사량
    return w<=0 or l_0<=0

#기초대사량 변화 고려한 다이어트
def diet_meta(w_0,d,l_0,l,a,t):
    w=w_0
    meta=l_0
    for _ in range(d):
        lamd=l-(meta+a) #체중의 변화
        w+=lamd
        if abs(lamd)>t:
            meta+=lamd//2
        if is_death(w,meta):
            return ['Danger Diet']
    #요요 판단
    if is_yoyo(meta,l_0,0):
        yoyo='YOYO'
    else:
        yoyo='NO'
    return w,meta,yoyo


#기초대사량 변화 고려하지 않은 다이어트
def diet_non(w_0,d,l_0,l,a): #초기체중, 날짜, 기초대사량, 에너지 소비량, 활동 대사량
    lamd=l-(l_0+a)
    w=w_0+lamd*d
    if is_death(w,l_0):
        return ['Danger Diet']
    else:
        return w,l_0
    
w_0,l_0,t=map(int,input().split())
d,l,a=map(int,input().split())
print(*diet_non(w_0,d,l_0,l,a))
print(*diet_meta(w_0,d,l_0,l,a,t))
