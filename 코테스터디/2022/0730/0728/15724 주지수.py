import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        graph[i][j + 1] = tmp[j]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        graph[i][j] += graph[i][j - 1]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        graph[j][i] += graph[j - 1][i]

for i in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    answer = graph[sx - 1][sy - 1] + graph[ex][ey] - graph[sx - 1][ey] - graph[ex][sy - 1]

    print(answer)
