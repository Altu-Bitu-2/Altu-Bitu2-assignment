import sys
#sys.stdin=open("input.txt",'r')
lines = sys.stdin.readlines()

def postorder(root, tree):  # 후위 순회
    if root == None:
        return
    postorder(tree[root][0], tree)
    postorder(tree[root][1], tree)
    print(root)


#전위 순회 결과로 트리 만들기
tree = dict()
root = int(lines[0])
tree[root] = [None, None]

for key in lines[1:]:
    parent = root
    key = int(key)
    tree[key] = [None, None]

    #key가 들어갈 위치 찾기
    while True:
        #root보다 key값이 작으면
        if key < parent:
            #삽입 가능
            if not tree[parent][0]:
                tree[parent][0] = key
                break
            #이미 다른 값이 있으면
            else:
                parent = tree[parent][0]
        else:
            #삽입 가능
            if not tree[parent][1]:
                tree[parent][1] = key
                break
            #이미 다른 값이 있으면
            else:
                parent = tree[parent][1]

postorder(root, tree)