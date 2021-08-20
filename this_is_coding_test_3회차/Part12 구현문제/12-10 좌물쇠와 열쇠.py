def nlock(lock):
    n = len(lock)
    newlock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            newlock[i + len(lock)][j + len(lock)] = lock[i][j]
    return newlock


def turn(key):
    tkey = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            tkey[i][j] = key[len(key) - 1 - j][i]
    return tkey


def check(x, y, lock, key):
    dlock = [[0] * len(lock) for _ in range(len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock)):
            dlock[i][j] = lock[i][j]

    cnt = 0
    for i in range(len(key)):
        for j in range(len(key)):
            dlock[x + i][y + j] += key[i][j]

    for i in range(len(lock) // 3, len(lock) * 2 // 3):
        for j in range(len(lock) // 3, len(lock) * 2 // 3):
            if dlock[i][j] == 1:
                cnt += 1
    if cnt == (len(lock) // 3) ** 2:
        return True
    return False


def solution(key, lock):
    lock = nlock(lock)

    Lenlock = len(lock)
    Lenkey = len(key)
    for i in range(4):
        key = turn(key)
        for i in range(Lenlock - Lenkey):
            for j in range(Lenlock - Lenkey):
                if check(i, j, lock, key):
                    return True
    return False