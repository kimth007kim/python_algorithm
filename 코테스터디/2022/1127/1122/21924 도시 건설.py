import sys
from collections import deque


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph=[]
result = 0
for i in range(m):
    a, b, c = map(int, input().split())
    result+=c
    graph.append([c,a,b])
graph.sort()

total=0
for c,a,b in graph:
    if find(a)!=find(b):
        union(a,b)
    else:
        total+=c

p=0
answer=True
for i in range(1,n+1):
    if i==1:
        p=find(parent[i])
    else:
        if p!=find(parent[i]):
            answer=False
            break
if answer ==True:
    print(total)
else:
    print(-1)