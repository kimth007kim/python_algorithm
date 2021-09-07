import heapq

INF = int(1e9)


def solution(n, s, a, b, fares):
    def dijkstra(s):
        distance = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, s))
        distance[s] = 0
        while q:
            dist, now = heapq.heappop(q)
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] < cost:
                    continue
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        return distance

    graph = [[] for _ in range(n + 1)]
    answer = 0
    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    data = dijkstra(s)
    answer += data[a] + data[b]
    for i in range(1, len(data)):
        if i == s or data[i] == INF:
            continue
        tmp = dijkstra(i)
        value = data[i] + tmp[a] + tmp[b]
        answer = min(answer, value)

    return answer