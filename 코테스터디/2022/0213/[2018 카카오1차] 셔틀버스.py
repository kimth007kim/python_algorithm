from collections import deque


def time_to_int(time):
    hr, mm = map(int, time.split(":"))
    result = hr * 60 + mm
    return result


def int_to_time(time):
    result = ""
    hr = (time // 60)
    if hr < 10:
        result += "0"
    result += str(hr)
    result += ":"
    mm = (time % 60)
    if mm < 10:
        result += "0"
    result += str(mm)

    return result


def choosing(arr, c, n, t, m):
    start = 540
    _arr = arr[:]
    _arr.append([c, 1])
    _arr.sort()
    q = deque(_arr)
    cnt = n
    while q:
        if cnt == 0:
            break
        for i in range(m):
            if q[0][0] > start:
                continue
            if len(q) == 0:
                break
            tmp = q.popleft()
            if tmp == c:
                return c
        cnt -= 1
        start += t
    if [c, 1] not in q:
        able.append(c)
    return -1


def solution(n, t, m, timetable):
    global able
    able = []

    cand = []
    bus = []

    arr = []

    for i in timetable:
        temp = time_to_int(i)
        arr.append([temp, 0])
        cand.append(temp)
        if temp - 1 >= 0:
            cand.append(temp - 1)
        if temp + 1 <= 1439:
            cand.append(temp + 1)

    tmp = 540
    bus.append(tmp)
    for i in range(n - 1):
        tmp += t
        bus.append(tmp)

    for busTime in bus:
        cand.append(busTime)
        if busTime - 1 >= 0:
            cand.append(busTime - 1)
        if busTime + 1 <= 1439:
            cand.append(busTime + 1)

    cand = list(set(cand))
    for c in cand:
        choice = choosing(arr, c, n, t, m)
        if choice != -1:
            able.append(choice)

    able.sort(reverse=True)

    return int_to_time(able[0])