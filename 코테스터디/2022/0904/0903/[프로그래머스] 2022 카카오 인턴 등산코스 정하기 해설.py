from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    pq = []
    graph = [[] for _ in range(n + 1)]
    visited = [int(1e9)] * (n + 1)
    summits.sort()
    summits_set = set(summits)
    for a, b, c, in paths:
        graph[a].append([c, b])
        graph[b].append([c, a])
    print(graph)
    for gate in gates:
        heappush(pq, (0, gate))
        visited[gate] = 0

    print(visited)
    while pq:
        intensity, now = heappop(pq)
        if visited[now] < intensity or now in summits_set:
            continue
        for weight, next_node in graph[now]:
            print(weight, next_node)
            next_val = max(intensity, weight)
            if next_val < visited[next_node]:
                visited[next_node] = next_val
                heappush(pq, (next_val, next_node))
    answer = [0, int(1e9)]
    print(visited)
    for summit in summits:
        print("==", summit)
        if visited[summit] < answer[1]:
            answer[0] = summit
            answer[1] = visited[summit]
    return answer