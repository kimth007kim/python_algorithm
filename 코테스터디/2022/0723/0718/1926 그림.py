from collections import deque
import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def find(graph, visited, x, y):
    cnt = 0
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        tx, ty = q.popleft()
        cnt += 1
        for i in range(4):
            nx = dx[i] + tx
            ny = dy[i] + ty
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx, ny])

    return cnt


n, m = map(int, input().split())
graph = []
visited = [[False] * (m) for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
MAX = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            size = find(graph, visited, i, j)
            MAX = max(MAX, size)
            answer += 1

print(answer)
print(MAX)
