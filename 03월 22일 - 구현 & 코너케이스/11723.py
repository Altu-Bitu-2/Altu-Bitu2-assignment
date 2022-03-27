import sys
input=sys.stdin.readline
all=set(str(i) for i in range(1,21))
s=set()

m=int(input())
for _ in range(m):
    cmd=list(input().split())

    if cmd[0]=='add':
        s.add(cmd[1])
        
    elif cmd[0]=='remove':
        if cmd[1] in s:
            s.remove(cmd[1])

    elif cmd[0]=='check':
        print(1 if cmd[1] in s else 0)

    elif cmd[0]=='toggle':
        if cmd[1] in s:
            s.remove(cmd[1])
        else:
            s.add(cmd[1])

    elif cmd[0]=='all':
        s=all

    elif cmd[0]=='empty':
        s=set()


