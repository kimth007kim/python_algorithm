from collections import deque
import copy


def bfs(x, y, game_board, visited, puzzle, number):
    LENGTH = len(game_board)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    storage = []
    storage.append((x, y))
    visited[x][y] = True
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < LENGTH and 0 <= ny < LENGTH:
                if game_board[nx][ny] == number and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    storage.append((nx, ny))
    return sorted(storage)


def zeroPosition(block, length):
    change = []
    minx = length
    miny = length
    for i in block:
        minx = min(minx, i[0])
        miny = min(miny, i[1])
    for x, y in block:
        change.append([x - minx, y - miny])
    return sorted(change)


def rotate(b, LENGTH):
    new_board = []
    for block in b:
        new_board.append([block[1], LENGTH - 1 - block[0]])
    return sorted(zeroPosition(new_board, LENGTH))


def solution(game_board, table):
    answer = []
    LENGTH = len(game_board)
    visited = [[False] * LENGTH for _ in range(LENGTH)]

    puzzle = []
    for i in range(LENGTH):
        for j in range(LENGTH):
            if game_board[i][j] == 1 and not visited[i][j]:
                puzzle.append(bfs(i, j, game_board, visited, puzzle, 1))

    visited = [[False] * LENGTH for _ in range(LENGTH)]
    empty = []
    for i in range(LENGTH):
        for j in range(LENGTH):
            if game_board[i][j] == 0 and not visited[i][j]:
                empty.append(bfs(i, j, game_board, visited, puzzle, 0))
    blocks = []
    for piece in puzzle:
        blocks.append(zeroPosition(piece, LENGTH))

    def match(block):
        for x in range(LENGTH):
            for y in range(LENGTH):
                move = []
                for _x, _y in block:
                    new_x = x + _x
                    new_y = y + _y
                    if new_x >= 0 and new_y >= 0:
                        try:
                            _ = game_board[x + _x][y + _y]
                            move.append((x + _x, y + _y))
                            print(move)
                        except IndexError:
                            break
                    else:
                        break
                if len(block) == len(move) and move in empty:
                    empty.remove(move)
                    answer.extend(move)
                    return True
        return False

    for block in blocks:
        for _ in range(4):
            if match(block) == False:
                block = rotate(block, LENGTH)
            else:
                break

    return len(answer)