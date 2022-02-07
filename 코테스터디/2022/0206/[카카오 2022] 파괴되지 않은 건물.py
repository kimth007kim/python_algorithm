def solution(board, skill):
    answer = 0

    graph = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, x1, y1, x2, y2, damage in skill:
        if t == 1:
            graph[x1][y1] -= damage
            graph[x2 + 1][y1] += damage
            graph[x1][y2 + 1] += damage
            graph[x2 + 1][y2 + 1] -= damage
        else:
            graph[x1][y1] += damage
            graph[x2 + 1][y1] -= damage
            graph[x1][y2 + 1] -= damage
            graph[x2 + 1][y2 + 1] += damage

    # 가로
    for i in range(len(graph)):
        total = graph[i][0]
        for j in range(1, len(graph[0])):
            total += graph[i][j]
            graph[i][j] = total

    # 세로
    for j in range(len(graph[0])):
        total = graph[0][j]
        for i in range(1, len(graph)):
            total += graph[i][j]
            graph[i][j] = total

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += graph[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer