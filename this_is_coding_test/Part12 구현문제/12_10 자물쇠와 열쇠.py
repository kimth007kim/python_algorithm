link="https://programmers.co.kr/learn/courses/30/lessons/60059"
key= [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock= [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
output=True
def solution(key, lock):
    cnt = 0
    hlist = gethole(lock, cnt)
    cnt += 1
    klist = gethole(key, cnt)
    print(klist)

    answer = False
    return answer


def turn(key):
    print(len(key))


def gethole(lock, cnt):
    if cnt == 0:
        a = 0
    else:
        a = 1
    result = []
    _lock = len(lock)
    for i in range(_lock):
        for j in range(_lock):
            if lock[i][j] == a:
                result.append([i, j])
    return result