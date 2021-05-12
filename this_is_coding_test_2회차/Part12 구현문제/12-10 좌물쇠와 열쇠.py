import copy

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
import copy


def solution(key, lock):
    answer = False
    length = len(lock)
    largelock = [[0] * (length * 3) for i in range(length * 3)]

    for i in range(length):
        for j in range(length):
            largelock[i + length][j + length] = lock[i][j]

    for i in range(4):
        key = rotation(key)
        for x in range(1, (length * 3 - length - 1)):
            for y in range(1, (length * 3 - length - 1)):
                copylock = copy.deepcopy(largelock)
                cnt = 0
                for a in range(len(key)):
                    for b in range(len(key)):
                        copylock[x + a][y + b] += key[a][b]
                for x1 in range(length, length * 2):
                    for y1 in range(length, length * 2):
                        if copylock[x1][y1] > 0:
                            cnt += 1

                if cnt == length * length:
                    return True
    return answer


def rotation(key):
    newKey = [[0] * len(key) for i in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            newKey[i][j] = key[len(key) - j - 1][i]
    return newKey


print(solution(key, lock))