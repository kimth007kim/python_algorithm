import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = []


def turn(graph, n, m, cnt):
    sx = 0 + cnt
    sy = 0 + cnt
    ex = n - cnt
    ey = m - cnt
    prev = graph[sx][sy]
    for i in range(sx + 1, ex):
        next =graph[i][sy]
        graph[i][sy] = prev
        prev =next
    for i in range(sy + 1, ey):
        next = graph[ex-1][i]
        graph[ex - 1][i] = prev
        prev = next
    for i in range(ex - 2, sx - 1, -1):
        next =graph[i][ey-1]
        graph[i][ey - 1] = prev
        prev = next
    for i in range(ey - 2, sy - 1, -1):
        next = graph[sx][i]
        graph[sx][i] = prev
        prev = next

    return graph


for i in range(n):
    graph.append(list(map(int, input().split())))
round = n*2+m*2-4
for i in range(min(n//2,m//2)):
    for j in range(r%(round-8*i)):

        graph = turn(graph, n, m, i)

for i in graph:
    print(*i)
