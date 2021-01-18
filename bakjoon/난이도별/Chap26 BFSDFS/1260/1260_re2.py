from collections import deque

n,m,v= map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in graph:
    j.sort()


def dfs(v):
    visited[v]=True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(v):
    q= deque()
    q.append(v)
    visited[v]=True

    while q:
        v= q.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

visited=[False]* (n+1)
dfs(v)
print()
visited=[False]* (n+1)
bfs(v)