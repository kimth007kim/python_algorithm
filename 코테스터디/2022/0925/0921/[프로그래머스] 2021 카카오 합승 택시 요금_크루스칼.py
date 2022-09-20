def solution(n, s, a, b, fares):
    inf = int(1e9)
    answer = int(1e11)
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for x, y, z in fares:
        graph[x][y] = z
        graph[y][x] = z

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                graph[y][z] = min(graph[y][z], graph[y][x] + graph[x][z])
    for i in range(1, n + 1):
        value = graph[i][s] + graph[i][a] + graph[i][b]
        answer = min(answer, value)
    return answer