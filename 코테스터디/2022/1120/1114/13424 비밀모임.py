import sys

input = sys.stdin.readline


def floyd(n, m):
    INF = int(1e11)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    MIN = INF
    where = n
    f = int(input())
    people = list(map(int, input().split()))
    for i in range(1, n + 1):
        tmp = 0
        for j in people:
            tmp += graph[i][j]
        if tmp < MIN:
            MIN = tmp
            where = i
    print(where)

for i in range(int(input())):
    n, m = map(int, input().split())
    floyd(n, m)
