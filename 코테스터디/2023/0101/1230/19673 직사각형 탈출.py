from collections import deque

import sys


def check(x, y, l):
    # print()
    if l == 0:
        for i in range(x, x + h + 1):
            if graph[i][y + w] == 1:
                return False
        return True
    if l == 2:
        for i in range(x, x + h + 1):
            if graph[i][y] == 1:
                return False
        return True

    if l == 1:
        for i in range(y, y + w + 1):
            if graph[x + h][i] == 1:
                return False
        return True
    if l == 3:
        for i in range(y, y + w + 1):
            if graph[x][i] == 1:
                return False
        return True


input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

h, w, sx, sy, ex, ey = map(int, input().split())
h, w, sx, sy, ex, ey = h - 1, w - 1, sx - 1, sy - 1, ex - 1, ey - 1

q = deque()
visited[sx][sy] = True

q.append([sx, sy, 0])
answer = -1
while q:
    # print(q)
    x, y, cnt = q.popleft()

    if x == ex and y == ey:
        answer = cnt
        break
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 > nx or 0 > ny or nx >= n or ny >= m:
            continue
        if visited[nx][ny] == True:
            continue
        tx, ty = nx + h, ny + w
        if 0 > tx or 0 > ty or tx >= n or ty >= m:
            continue
        if check(nx, ny, i) == False:
            continue
        q.append([nx, ny, cnt + 1])
        visited[nx][ny] = True

print(answer)
