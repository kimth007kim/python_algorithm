def dfs(visited, sheep, wolf):
    global n, graph, data, answer
    answer = max(answer, sheep)
    for i in visited:
        for j in graph[i]:
            if j in visited:
                continue
            s, w = sheep, wolf
            if data[j] == 0:
                s += 1
            else:
                w += 1
            if s <= w:
                continue
            visited.add(j)
            dfs(visited, s, w)
            visited.remove(j)


def solution(info, edges):
    global n, graph, data, answer

    data = info
    answer = 0
    n = len(info)
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    visited.add(0)
    dfs(visited, 1, 0)

    return answer