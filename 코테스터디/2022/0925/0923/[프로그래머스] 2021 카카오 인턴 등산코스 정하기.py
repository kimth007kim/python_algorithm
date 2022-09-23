from heapq import heappush, heappop


def solution(n, paths, gates, summits):
    INF = int(1e10)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    summit_set = set()
    for i in summits:
        summit_set.add(i)
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    hq = []
    for i in gates:
        heappush(hq, [0, i])
        distance[i] = 0
    while hq:
        dist, now = heappop(hq)
        if now in summit_set or distance[now] < dist:
            continue
        for n, d in graph[now]:
            tmp = max(dist, d)
            if distance[n] > tmp:
                distance[n] = tmp
                heappush(hq, [tmp, n])

    node = -1
    val = INF
    summits.sort()
    for n in summits:
        v = distance[n]
        if v < val:
            node = n
            val = v

    answer = [node, val]
    return answer