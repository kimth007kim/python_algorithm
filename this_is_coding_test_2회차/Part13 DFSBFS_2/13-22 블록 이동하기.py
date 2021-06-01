board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result=7

from collections import deque

def solution(board):
    n = len(board)
    newboard = [[1] * (n + 2) for i in range(n + 2)]
    for i in range(n):
        for j in range(n):
            newboard[i + 1][j + 1] = board[i][j]

    for i in newboard:
        print(i)
    print()
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    # pos = {(3, 3), (3, 4)}
    q.append((pos, 0))
    visited.append(pos)
    # print("visited=", visited)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            print("정답", pos)
            return cost
        print(pos, cost)
        for next_pos in getpos(pos, newboard):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


def getpos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        pos1_nx, pos1_ny, pos2_nx, pos2_ny = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next_pos.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})
    if pos1_x == pos2_x:
        # 가로
        # 좌상단
        if board[pos2_x - 1][pos2_y] != 1:
            if board[pos1_x - 1][pos1_y] != 1 and board[pos1_x][pos1_y] != 1:
                next_pos.append({(pos1_x - 1, pos1_y), (pos1_x, pos1_y)})
                print((pos1_x - 1, pos1_y), (pos1_x, pos1_y))
        # 우상단
        if board[pos1_x - 1][pos1_y] != 1:
            if board[pos2_x][pos2_y] != 1 and board[pos2_x + 1][pos2_y] != 1:
                next_pos.append({(pos2_x - 1, pos2_y), (pos2_x, pos2_y)})
                print((pos2_x - 1, pos2_y), (pos2_x, pos2_y))
        # 좌하단
        if board[pos2_x + 1][pos2_y] != 1:
            if board[pos1_x][pos1_y] != 1 and board[pos1_x + 1][pos1_y] != 1:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + 1, pos1_y)})
                print((pos1_x, pos1_y), (pos1_x + 1, pos1_y))
        # 우하단
        if board[pos1_x + 1][pos1_y] != 1:
            if board[pos2_x][pos2_y] != 1 and board[pos2_x + 1][pos2_y] != 1:
                next_pos.append({(pos2_x, pos2_y), (pos2_x + 1, pos2_y)})
                print((pos2_x, pos2_y), (pos2_x + 1, pos2_y))
    else:
        # 세로
        # 좌상단
        if board[pos2_x][pos2_y - 1] != 1:
            if board[pos1_x][pos1_y - 1] != 1 and board[pos1_x][pos1_y] != 1:
                next_pos.append({(pos1_x, pos1_y - 1), (pos1_x, pos1_y)})
                print((pos1_x, pos1_y - 1), (pos1_x, pos1_y))
        # 우상단
        if board[pos1_x][pos1_y + 1] != 1:
            if board[pos2_x][pos2_y] != 1 and board[pos2_x][pos2_y + 1] != 1:
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + 1)})
                print((pos2_x, pos2_y), (pos2_x, pos2_y + 1))
        # 좌하단
        if board[pos2_x][pos2_y + 1] != 1:
            if board[pos1_x][pos1_y] != 1 and board[pos1_x][pos1_y + 1] != 1:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + 1)})
                print((pos1_x, pos1_y), (pos1_x, pos1_y + 1))
        # 우하단
        if board[pos1_x - 1][pos1_y] != 1:
            if board[pos2_x][pos2_y - 1] != 1 and board[pos2_x][pos2_y] != 1:
                next_pos.append({(pos2_x, pos2_y - 1), (pos2_x, pos2_y)})
                print((pos2_x, pos2_y - 1), (pos2_x, pos2_y))

                # print(next_pos)
    return next_pos


print(solution(board))