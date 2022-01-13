from collections import deque


def Opposite(direction):
    result = (direction + 2) % 4
    return result


def show(arr):
    if len(arr) == 8:
        print("--------------------------")
        print()
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == int(1e9):
                    print("XXXX", end=" ")
                else:
                    l = len(str(arr[i][j]))

                    print(" " * (4 - l) + str(arr[i][j]), end=" ")
            print()
        print("--------------------------")


def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    INF = int(1e9)
    n = len(board)
    visited = [[INF] * n for _ in range(n)]
    visited[0][0] = 0

    q = deque()
    cnt = 0
    for i in range(1, 3):
        q.append([0, 0, 0, i])
    while q:
        print(q)
        x, y, total, direction = q.popleft()
        print("=====       x={} y={} total={} dirction={}".format(x, y, total, direction))
        op = Opposite(direction)
        for i in range(4):
            tmp = 0
            if i != op:
                nx = dx[i] + x
                ny = dy[i] + y
                if direction != i:
                    tmp = total + 600
                else:
                    tmp = total + 100
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = tmp
                        q.append([nx, ny, tmp, i])

                        show(visited)
    show(visited)
    return visited[n - 1][n - 1]