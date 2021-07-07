# import heapq
from collections import deque

INF = int(1e9)


def solution(n, edge):
    distance = [INF] * (n + 1)
    graph = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)
    # for i in range(len(edge)):
    #     print(i)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)

    q = deque([1])
    distance[1] = 0
    while q:
        # print(q)
        a = q.popleft()
        # print(a)
        for i in graph[a]:
            distance[i] = min(distance[i], distance[a] + 1)
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    distance = distance[1:]
    maximum = -1
    cnt = 0
    for i in range(len(distance)):
        if distance[i] > maximum:
            maximum = distance[i]
            cnt = 1
            continue
        if distance[i] == maximum:
            cnt += 1

    return cnt