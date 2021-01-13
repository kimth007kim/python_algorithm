# from collections import deque
#
# N,M,V= map(int,input().split())
#
# graph=[[] for _ in range(N+1)]
# for i in range(M):
#     D,S= map(int,input().split())
#
#     graph[D].append(S)
#     graph[S].append(D)
#
# for j in range(N+1):
#     graph[j]=list(set(graph[j]))
#     if j in graph[j]:
#         graph[j].remove(j)
#
# def dfs(graph, v, visited1):
#     visited1[v]= True
#     print(v,end=" ")
#
#     for i in graph[v]:
#         if not visited1[i]:
#             dfs(graph,i,visited1)
#
# def bfs(graph,start,visited2):
#     queue = deque([start])
#     visited2[start]=True
#
#
#     while queue:
#         v= queue.popleft()
#         print(v, end=' ')
#
#         for i in graph[v]:
#             if not visited2[i]:
#                 queue.append(i)
#                 visited2[i]=True
#
# visited1=[False]* (N+1)
# visited2=[False]* (N+1)
#
# dfs(graph,V,visited1)
# print()
# bfs(graph,V,visited2)

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

dfs(v)
print()
bfs(v)
