from collections import deque


def solution(n, computers):
    # print(computers)
    visited = [False] * (n)
    cnt = 0
    graph = [[] for _ in range(n)]
    # print(visited)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    for i in range(n):
        if not visited[i]:
            cnt += 1
            bfs(graph, i, visited)
    # print(visited,cnt)
    return cnt


def bfs(graph, x, visited):
    q = deque([x])
    while q:
        x = q.popleft()
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

