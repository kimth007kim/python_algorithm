from itertools import permutations
from collections import defaultdict
from collections import deque


def move(graph, sx, sy, ex, ey):
    q = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[int(1e9)] * 4 for _ in range(4)]
    q.append([sx, sy, 0])
    visited[sx][sy] = 0
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 4 and 0 <= ny < 4:
                if visited[nx][ny] > cnt + 1:
                    visited[nx][ny] = cnt + 1
                    q.append([nx, ny, cnt + 1])

            tx, ty = x, y
            while 0 <= tx < 4 and 0 <= ty < 4:
                tx += dx[i]
                ty += dy[i]
                if not (0 <= tx < 4 and 0 <= ty < 4):
                    if visited[tx - dx[i]][ty - dy[i]] > cnt + 1:
                        visited[tx - dx[i]][ty - dy[i]] = cnt + 1
                        q.append([tx - dx[i], ty - dy[i], cnt + 1])
                    break
                if graph[tx][ty] != 0:
                    if visited[tx][ty] > cnt + 1:
                        visited[tx][ty] = cnt + 1
                        q.append([tx, ty, cnt + 1])
                    break
    return visited[ex][ey]


def solution(board, r, c):
    point = defaultdict(list)
    answer = int(1e9)
    idx = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                idx.add(board[i][j])
                point[board[i][j]].append([i, j])
    per = list(permutations(list(idx), len(list(idx))))

    for p in per:
        total = 0
        graph = [[0] * 4 for _ in range(4)]
        sx, sy = r, c
        for a in range(4):
            for b in range(4):
                graph[a][b] = board[a][b]
        for j in p:

            left = move(graph, sx, sy, point[j][0][0], point[j][0][1]) + move(graph, point[j][0][0], point[j][0][1],
                                                                              point[j][1][0], point[j][1][1])
            right = move(graph, sx, sy, point[j][1][0], point[j][1][1]) + move(graph, point[j][1][0], point[j][1][1],
                                                                               point[j][0][0], point[j][0][1])
            # print(j,"==",left,right, "----",total)
            if left > right:
                graph[point[j][1][0]][point[j][1][1]] = 0
                total += 1
                total += right
                sx, sy = point[j][0][0], point[j][0][1]
                graph[point[j][0][0]][point[j][0][1]] = 0
                total += 1
            else:
                total += 1
                graph[point[j][0][0]][point[j][0][1]] = 0
                total += left
                sx, sy = point[j][1][0], point[j][1][1]
                graph[point[j][1][0]][point[j][1][1]] = 0
                total += 1
        answer = min(answer, total)

    return answer