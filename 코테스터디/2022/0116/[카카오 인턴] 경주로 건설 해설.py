import math
from collections import deque


def solution(board):
    def bfs(start):
        # table[y][x] = 해당 위치에 도달하는 최솟값.
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
        print(table)
        # 진행 방향. 위 - 0, 왼쪽 - 1, 아래 = 2, 오른쪽 = 3
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque([start])

        # 처음 위치의 비용 = 0
        table[0][0] = 0
        while queue:
            # y좌표, x좌표, 비용, 진행방향
            y, x, cost, head = queue.popleft()
            for idx, (dy, dx) in enumerate(dirs):
                ny, nx = y + dy, x + dx
                # 진행방향과 다음 방향이 일치하면 + 100, 다르면 전환비용 500 + 진행비용 100 = 600
                n_cost = cost + 600 if idx != head else cost + 100
                # board[y][x] == 0 : 진행방향에 벽이 없음. table[ny][nx] > n_cost : 다음 좌표의 최솟값보다 진행방향 비용이 작을 경우
                if 0 <= ny < len(board) and 0 <= nx < len(board) and board[ny][nx] == 0 and table[ny][nx] > n_cost:
                    # table 좌표 업데이트.
                    table[ny][nx] = n_cost
                    queue.append((ny, nx, n_cost, idx))
        return table[-1][-1]

    return min(bfs((0, 0, 0, 2)), bfs((0, 0, 0, 3)))