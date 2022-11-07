from collections import deque

import sys

input =sys.stdin.readline


n,m =map(int,input().split())
graph= [[] for _ in range(n+1)]
visited= [0 for _ in range(n+1)]
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if visited[i]==0:
        q=deque()
        q.append(i)
        visited[i]=1
        while q:
            x= q.popleft()
            for j in graph[x]:
                if visited[j]==0:
                    visited[j]=visited[x]*-1
                    q.append(j)
                    print(visited)
                elif visited[j]==visited[x]:
                    print(0)
                    exit(0)
print(1)
print(graph,visited)