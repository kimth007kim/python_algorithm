import sys


def count(graph):
    total = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                total += graph[i][j]
    return total


def turnDown(down, graph):
    sx, sy = down
    prev = 0
    for i in range(1, c):
        _next = graph[sx][i]
        graph[sx][i] = prev
        prev = _next
    for i in range(sx+1, r):
        _next = graph[i][c - 1]
        graph[i][c - 1] = prev
        prev = _next
    for i in range(c - 2, -1, -1):
        _next = graph[r - 1][i]
        graph[r - 1][i] = prev
        prev = _next
    for i in range(r - 2, sx, -1):
        _next = graph[i][0]
        graph[i][0] = prev
        prev = _next


def turnUp(up, graph):
    ex, ey = up
    prev = 0
    for i in range(1, c):
        _next = graph[ex][i]
        graph[ex][i] = prev
        prev = _next
    for i in range(ex-1, -1, -1):
        _next = graph[i][c - 1]
        graph[i][c - 1] = prev
        prev = _next
    for i in range(c - 2, -1, -1):
        _next = graph[0][i]
        graph[0][i] = prev
        prev = _next
    for i in range(1, ex):
        _next = graph[i][0]
        graph[i][0] = prev
        prev = _next


def checkCand(graph):
    cand = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1 and graph[i][j] != 0:
                value = graph[i][j]
                cnt = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        cnt += 1
                        cand.append([nx, ny, value // 5])
                # print(i,j,"===",value,cnt)
                graph[i][j] = value - (value // 5) * cnt
                # print(graph[i][j])
    return cand


input = sys.stdin.readline

r, c, t = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
graph = []
up = [0, 0]
down = [0, 0]
u = 0
for i in range(r):
    graph.append(list(map(int, input().split())))
for i in range(r):
    if graph[i][0] == -1:
        if u == 0:
            up = [i, 0]
            u = 1
        else:
            down = [i, 0]
            break

for _ in range(t):
    cand = checkCand(graph)
    # print(cand)
    # show(graph)
    for a, b, d in cand:
        graph[a][b] += d
    turnDown(down, graph)
    turnUp(up, graph)
print(count(graph))
