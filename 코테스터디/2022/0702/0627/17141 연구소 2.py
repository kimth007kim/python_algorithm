from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def copy(arr):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = arr[i][j]
    return result


def calc(arr, c):
    global answer
    graph = copy(arr)
    q = deque()
    for i, j in c:
        graph[i][j] = 0
        q.append([i, j, 0])

    while q:
        x, y, now = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1:
                if graph[nx][ny] == -2:
                    graph[nx][ny] = now + 1
                    q.append([nx, ny, now + 1])
                else:
                    if graph[nx][ny] > now + 1:
                        graph[nx][ny] = now + 1
                        q.append([nx, ny, now + 1])

    MAX = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] ==-2:
                return
            MAX = max(graph[i][j], MAX)
    answer.append(MAX)
    return


n, m = map(int, input().split())
virus = []
arr = []
answer = []
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp_list = []
    for j in range(n):
        if tmp[j] == 0 or tmp[j] == 2:
            tmp_list.append(-2)
        else:
            tmp_list.append(-1)
        if tmp[j] == 2:
            virus.append([i, j])
    arr.append(tmp_list)

comb = list(combinations(virus, m))

for c in comb:
    calc(arr, c)
if len(answer) == 0:
    print(-1)
else:
    print(min(answer))
