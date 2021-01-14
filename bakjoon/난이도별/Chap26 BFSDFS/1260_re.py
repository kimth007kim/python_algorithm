from collections import deque

n,m,v = map(int,input().split())

visited1= [False]*(n+1)
visited2= [False]*(n+1)


graph=[[] for _ in range(n+1)]
for i in range(m):
    s,d = map(int,input().split())
    graph[s].append(d)
    graph[d].append(s)


for k in graph:
    k.sort()

def bfs(graph,start,visited2):
    queue=deque([start])
    visited2[start]=True

    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

def dfs(graph,v,visited1):
    visited1[v]=True
    print(v,end=" ")

    for j in graph[v]:
        if not visited1[j]:
            dfs(graph,j,visited1)

dfs(graph,v,visited1)
print()
bfs(graph,v,visited2)