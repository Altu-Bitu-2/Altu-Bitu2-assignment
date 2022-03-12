import sys
#sys.stdin=open("input.txt","r")
lines = sys.stdin.readlines()

s,e,q = lines[0].rstrip().split()

attend_list=set()
count=0 #출석한 사람 수

for line in lines[1:]:
    time,name=list(line.split())
    if time<=s: #개강총회 시작 전 출석
        attend_list.add(name)

    elif e<=time<=q: #개강총회 후 출석
        if name in attend_list:
            attend_list.remove(name)
            count+=1
        
print(count)
