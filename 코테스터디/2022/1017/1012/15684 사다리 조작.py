# https://www.acmicpc.net/problem/15684

from collections import deque
import sys

input = sys.stdin.readline

find = False


def check(graph):
    global find
    for start in range(1, n + 1):
        k = start
        for i in range(1, h + 1):
            if graph[i][k]==1:
                k+=1
            elif graph[i][k]==-1:
                k-=1
        if start!=k:
            return False
        # print(start)
    # q = deque()
    # for i in range(1, n + 1):
    #     q.append([0, i, i])
    # arr = []
    # while q:
    #     x, y, s = q.popleft()
    #     if x == h:
    #         arr.append([x,y,s])
    #         continue
    #     nx=x+1
    #     if graph[nx][y]==1:
    #         q.append([nx,y+1,s])
    #     elif graph[nx][y]==-1:
    #         q.append([nx,y-1,s])
    #     # print(x, y, s)
    #     else:
    #         q.append([nx,y,s])
    # for a,b,c in arr:
    #     if b!=c:
    #         return False
    find = True
    return True


def dfs(cnt, graph):
    global answer
    if check(graph) == True:
        answer = min(answer, cnt)
        return
    if answer <= cnt or cnt == 3:
        return
    # print(cnt)
    for i in range(1, h + 1):
        for j in range(1, n):
            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                graph[i][j] = 1
                graph[i][j + 1] = -1
                dfs(cnt + 1, graph)
                graph[i][j] = 0
                graph[i][j + 1] = 0


n, m, h = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(h + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[a][b + 1] = -1
if check(graph) == True:
    print(0)
else:
    answer = 4
    for i in range(1, h + 1):
        for j in range(1, n):
            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                graph[i][j] = 1
                graph[i][j + 1] = -1
                dfs(1, graph)
                graph[i][j] = 0
                graph[i][j + 1] = 0

    if find == True:
        print(answer)
    else:
        print(-1)
