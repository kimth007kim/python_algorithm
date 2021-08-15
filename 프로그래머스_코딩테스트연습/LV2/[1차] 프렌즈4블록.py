def checker(m, n, graph):
    for i in range(m - 1):
        for j in range(n - 1):
            if graph[i][j] == graph[i][j + 1] == graph[i + 1][j] == graph[i + 1][j + 1] and graph[i][j] != -1:
                return True


def maker(m, n, graph):
    copy_graph = [[0] * (n) for _ in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            if (graph[i][j] == graph[i][j + 1] == graph[i + 1][j] == graph[i + 1][j + 1]) and graph[i][j] != -1:
                copy_graph[i][j] = 1
                copy_graph[i][j + 1] = 1
                copy_graph[i + 1][j] = 1
                copy_graph[i + 1][j + 1] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if copy_graph[i][j] == 1:
                cnt += 1
                graph[i][j] = -1

    return graph, cnt


def move(graph):
    n = len(graph)
    m = len(graph[0])

    ngraph = [[-1] * m for i in range(n)]
    for i in range(m):
        cnt = 0
        for j in range(n - 1, -1, -1):
            if graph[j][i] != -1:
                ngraph[n - 1 - cnt][i] = graph[j][i]
                cnt += 1
    return ngraph


def solution(m, n, board):
    graph = []
    for i in board:
        graph.append(list(i))
    cnt = 0

    while checker(m, n, graph) == True:
        g, c = maker(m, n, graph)
        cnt += c
        graph = move(g)

    return cnt