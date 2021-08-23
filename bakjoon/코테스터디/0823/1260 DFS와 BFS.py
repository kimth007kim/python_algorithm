from collections import deque

n,m,v= map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for j in graph:
    j.sort()

def bfs(v):
    visited = [False] * (n + 1)
    q=deque()
    q.append(v)
    visited[v]=True
    while q:
        v= q.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

def dfs(v):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

visited=[False]*(n+1)
dfs(v)
print()
bfs(v)