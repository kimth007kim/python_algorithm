from heapq import heappush, heappop

def dajikstra(start):
    dist = [inf] * (N + 1)
    q = []
    heappush(q, [0, start])
    while q:
        d, now = heappop(q)
        if dist[now] > d:
            dist[now] = d
            for _next, _d in graph[now]:
                if dist[_next] >= d + _d:
                    heappush(q, [d + _d, _next])
    return dist


def solution(n, s, a, b, fares):
    global N, S, A, B, inf, graph

    inf = int(1e9)
    graph = [[] for _ in range(n + 1)]
    N, S, A, B = n, s, a, b
    for x, y, z in fares:
        graph[x].append([y, z])
        graph[y].append([x, z])
    sdist = dajikstra(s)
    adist = dajikstra(a)
    bdist = dajikstra(b)

    answer = adist[s] + bdist[s]

    for i in range(1, n + 1):
        if i == s or sdist[i] == inf or adist[i] == inf or bdist[i] == inf:
            continue
        answer = min(answer, sdist[i] + adist[i] + bdist[i])
    return answer