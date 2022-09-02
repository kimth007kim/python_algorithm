from collections import defaultdict


def dfs(now, start, value, visited):
    global MAX, road, result, check
    # print(check)
    if now in check:
        if value <= MAX:
            MAX = value
            if value not in result:
                result[value] = now
            else:
                result[value] = min(result[value], now)
        return

    for NEXT, cost in road[now]:

        # print(road[now])
        if cost > MAX:
            # print("안됨")
            continue
        if visited[NEXT] == False:
            # print(now,"->",NEXT,"=",cost)
            # print(now,"->",n,"=",cost)
            visited[NEXT] = True
            # print(visited)
            # print(now,n,value,visited)
            COST = max(cost, value)
            dfs(NEXT, start, COST, visited)
            visited[NEXT] = False


def solution(n, paths, gates, summits):
    global MAX, road, result, check

    check = defaultdict(int)
    for i in summits:
        check[i] = 1
    result = defaultdict(int)
    MAX = 200001

    road = [[] for _ in range(n + 1)]
    for a, b, c in paths:
        road[a].append([b, c])
        road[b].append([a, c])

    # print(road)
    visited = [False] * (n + 1)
    for j in gates:
        visited[j] = True
    for i in gates:
        dfs(i, i, 0, visited)

    if MAX not in result:
        return 0, MAX
    return result[MAX], MAX