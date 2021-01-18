from collections import deque

def dfs(v):
    print(v, end = ' ')
    visited[v] = True
    for e in arr[v]:
        if visited[e] == False:
            dfs(e)

def bfs(v):
    q = deque()
    print(q)
    q.append(v)
    print(q)
    visited[v] = True
    print(v, end = ' ')
    while q:
        v = q.popleft()
        for e in arr[v]:
            if visited[e] == False:
                q.append(e)
                visited[e] = True
                print(e, end = ' ')
#
# def bfs(graph,start,visited2):
#     queue=deque([start])
#     visited2[start]=True
#
#     while queue:
#         v = queue.popleft()
#         print(v,end=" ")
#         for i in graph[v]:
#             if not visited2[i]:
#                 queue.append(i)
#                 visited2[i]=True


n, m, v = map(int, input().split(' '))

arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split(' '))
    arr[x].append(y)
    arr[y].append(x)

for i in arr:
    i.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)