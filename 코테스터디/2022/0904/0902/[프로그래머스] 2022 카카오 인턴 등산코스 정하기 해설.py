from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    def get_min_intensity():
        pq = []
        visited = [int(1e9)] * (n + 1)

        for gate in gates:
            heappush(pq, (0, gate))
            visited[gate] = 0
        while pq:
            print(pq, visited)
            intensity, node = heappop(pq)
            print(intensity, node)
            if node in summits_set or intensity > visited[node]:
                continue
            for weight, next_node in graph[node]:
                new_intensity = max(intensity, weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(pq, (new_intensity, next_node))
        min_intensity = [0, int(1e9)]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        return min_intensity

    summits.sort()
    summits_set = set(summits)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    return get_min_intensity()