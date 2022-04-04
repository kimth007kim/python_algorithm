import sys


def traversal(now,tree,parent):
    print(now,tree,parent)
    for i in tree[now]:
        if parent[i]==0:
            parent[i]=now
            traversal(i,tree,parent)


input = sys.stdin.readline
n= int(input())
tree=[[] for _ in range(n+1)]
parent= [ 0 for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

traversal(1,tree,parent)
print(tree)
print(parent)

