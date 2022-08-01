from collections import deque
import sys

input= sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


def bfs(visited, graph, now):
    visit = [False] * (n + 1)
    q = deque()
    q.append([now, 0])
    while q:
        num, cnt = q.popleft()
        visited[now][num] = cnt
        for i in graph[num]:
            if visit[i] == False and visited[now][i] > cnt + 1:
                visit[i] = True
                q.append([i, cnt + 1])


for i in range(1, n + 1):
    bfs(visited, graph, i)
arr = []
MIN=int(1e9)
for i in range(1, n + 1):
    value=0
    for j in range(1, n + 1):
        if visited[i][j]!= int(1e9):
            value = max(value,visited[i][j])
    if value<MIN:
        MIN=value
        arr=[i]
    elif value==MIN:
        arr.append(i)


print(MIN,len(arr))
print(*arr)
