import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph,start,visited):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                print(visited)

n,m=map(int,input().split())
graph=[[]for i in range(n+1)]
visited=[False]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
cnt=0

answer=0
for i in range(1,n+1):
    if not visited[i]:
        bfs(graph,i,visited)
        answer+=1

print(answer)