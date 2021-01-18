from collections import deque

n= int(input())
m= int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
answer= []

for _ in range(m):
    x,y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in graph:
    j.sort()

def bfs(v):
    q= deque()
    q.append(v)
    visited[v]=True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                answer.append(i)



bfs(1)
print(len(answer))