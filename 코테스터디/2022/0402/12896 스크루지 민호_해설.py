import sys
import math
input = sys.stdin.readline

def traverse(prev,s,depth):
    global rad,node
    print("rad = {} node = {}".format(rad,node))
    print("prev = {} s = {} depth = {}".format(prev,s,depth))
    if rad<depth:
        rad=depth
        node =s

    for nxt in tree[s]:
        if prev == nxt:
            continue
        traverse(s,nxt,depth+1)

n= int(input())
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    x,y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

rad =0
node=0
traverse(0,1,0)
traverse(0, node, 0)
print(math.ceil(rad / 2))