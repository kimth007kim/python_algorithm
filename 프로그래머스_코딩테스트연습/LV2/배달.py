import heapq

INF = int(1e9)


def solution(N, road, K):
    tmp = [[INF] * (N + 1) for _ in range(N + 1)]
    for a, b, c in road:
        tmp[a][b] = min(tmp[a][b], c)
    roads = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if tmp[i][j] != INF:
                roads.append([i, j, tmp[i][j]])
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for a, b, c in roads:
        graph[a].append([b, c])
        graph[b].append([a, c])

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            distance[now] = dist
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    cnt = 0
    print(distance)
    for i in range(1, N + 1):
        if distance[i] <= K:
            cnt += 1

    return cnt