def dfs(now, cnt, visited, n):
    global MAX
    if now == len(losted):
        MAX = max(MAX, cnt)
        return
    p = losted[now]
    cand = []
    if p + 1 <= n:
        if visited[p + 1] > 1:
            cand.append(p + 1)
    if p - 1 > 0:
        if visited[p - 1] > 1:
            cand.append(p - 1)
    if len(cand) == 0:
        dfs(now + 1, cnt, visited, n)
        return
    for i in cand:
        visited[p] += 1
        visited[i] -= 1
        dfs(now + 1, cnt + 1, visited, n)
        visited[p] -= 1
        visited[i] += 1


def solution(n, lost, reserve):
    global dic, MAX, losted
    answer = 0
    dic = {}
    losted = []
    for i in range(1, n + 1):
        dic[i] = 1
    for i in lost:
        dic[i] -= 1
    for i in reserve:
        dic[i] += 1
    visited = [0] * (n + 1)

    for i in dic:
        visited[i] = dic[i]
        if dic[i] < 1:
            losted.append(i)
        else:
            answer += 1
    MAX = 0
    print(visited)
    dfs(0, 0, visited, n)

    return answer + MAX