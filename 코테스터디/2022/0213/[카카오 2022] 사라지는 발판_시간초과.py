from collections import deque


def graph_update(board, x, y):
    tmp = [[0] * row for _ in range(column)]
    for i in range(column):
        for j in range(row):
            tmp[i][j] = board[i][j]
    tmp[x][y] = 0
    return tmp


def solution(board, aloc, bloc):
    global column, row
    column = len(board)
    row = len(board[0])
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cand = []
    q = deque()
    q.append([aloc, bloc, board, 0])

    while q:
        A, B, graph, cnt = q.popleft()
        for i in range(4):
            ax = A[0] + dx[i]
            ay = A[1] + dy[i]
            if 0 > ax or ax >= column or 0 > ay or ay >= row or graph[ax][ay] == 0:
                cand.append(cnt)
            else:
                tmp = graph_update(board, ax, ay)
                for j in range(4):
                    bx = B[0] + dx[i]
                    by = B[1] + dy[i]
                    if 0 > bx or bx >= column or 0 > by or by >= row or tmp[bx][by] == 0:
                        cand.append(cnt)
                    else:
                        q.append([[ax, ay], [bx, by], tmp, cnt + 1])

    return answer