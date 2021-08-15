from collections import deque


def addStack(city, cacheSize, q):
    if len(q) < cacheSize:
        if city not in q:
            q.append(city)
            return 5
        else:
            q.remove(city)
            q.append(city)
            return 1


    elif len(q) == cacheSize:
        if city not in q:
            q.popleft()
            q.append(city)
            return 5
        else:
            q.remove(city)
            q.append(city)
            return 1


def solution(cacheSize, cities):
    time = 0
    q = deque()
    if cacheSize != 0:
        for i in cities:
            city = i.upper()
            time += addStack(city, cacheSize, q)
    else:
        time = len(cities) * 5

    return time