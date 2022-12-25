import sys

input = sys.stdin.readline


def find(parents, x):
    if parents[x] != x:
        return find(parents, parents[x])
    return parents[x]


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parents = [i for i in range(n)]
    arr = []
    total = 0
    for i in range(m):
        x, y, z = map(int, input().split())
        arr.append([z, x, y])
        total += z
    arr.sort()
    cost = 0
    for c, a, b in arr:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            cost += c

    print(total - cost)
