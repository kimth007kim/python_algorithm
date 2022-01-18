from collections import deque


def solution(board):
    n = len(board)
    direct = [[0, 1, 0], [1, 0, 1], [0, -1, 2], [-1, 0, 3]]
    INF = int(1e9)
    dp = [[[INF] * n for _ in range(n)] for _ in range(4)]
    for i in range(4):
        dp[i][0][0] = 0
    q = deque()
    q.append([0, 0, 0, 0])
    q.append([0, 0, 0, 1])
    while q:
        cost, x, y, d = q.popleft()
        for dx, dy, pd in direct:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                value = cost + 100
                if pd != d:
                    value += 500
                if dp[pd][nx][ny] > value:
                    dp[pd][nx][ny] = value
                    if nx == n - 1 and ny == n - 1:
                        continue
                    q.append([value, nx, ny, pd])

    answer = INF
    for i in range(4):
        if answer > dp[i][n - 1][n - 1]:
            answer = dp[i][n - 1][n - 1]
    return answer