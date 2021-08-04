def cacheAdd(cacheSize, cache, city):
    if city in cache:
        time = 1
        cache.remove(city)
        cache.append(city)
        # print(cache,city)
        return time
    else:
        time = 5
    # print(cache,city)

    if cacheSize == 0:
        return time
    if len(cache) < cacheSize:
        cache.append(city)
    elif len(cache) >= cacheSize:
        cache.pop(0)
        cache.append(city)
    return time


def solution(cacheSize, cities):
    city = []
    for i in cities:
        city.append(i.upper())

    time = 0
    cache = []
    for i in city:
        time += cacheAdd(cacheSize, cache, i)
        # print(time)
    return time