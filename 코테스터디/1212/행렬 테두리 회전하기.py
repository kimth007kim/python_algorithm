def solution(rows, columns, queries):
    graph = [[0] * columns for i in range(rows)]
    number = 1
    answer = []
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = number
            number += 1

    for sx, sy, ex, ey in queries:
        sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
        MAXIMUM = []
        left_top = graph[sx][sy]
        prev = left_top
        for i in range(sy, ey + 1):
            now = graph[sx][i]
            MAXIMUM.append(now)
            graph[sx][i] = prev
            prev = now
        for i in range(sx + 1, ex + 1):
            now = graph[i][ey]
            MAXIMUM.append(now)
            graph[i][ey] = prev
            prev = now
        for i in range(ey - 1, sy - 1, -1):
            now = graph[ex][i]
            MAXIMUM.append(now)
            graph[ex][i] = prev
            prev = now
        for i in range(ex - 1, sx - 1, -1):
            now = graph[i][sy]
            MAXIMUM.append(now)
            graph[i][sy] = prev
            prev = now
        MAXIMUM.sort()
        answer.append(MAXIMUM[0])

    return answer