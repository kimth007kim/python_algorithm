import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)
edges = []
for i in range(1, v + 1):
    parent[i] = i
for i in range(e):
    a, b, d = map(int, input().split())
    edges.append([d, a, b])

edges.sort()
total = 0
for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost

print(total)
