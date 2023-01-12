import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        return find(parents[x])
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)
answer = set()
for i in range(1, n + 1):
    tmp = find(i)
    answer.add(tmp)

print(len(answer))
