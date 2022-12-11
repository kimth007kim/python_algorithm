import sys
from collections import deque


input =sys.stdin.readline

INF = int(1e12)
a, b = map(int, input().split())

n, m = map(int, input().split())
visited=[INF]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q=deque()
q.append([a,0])
visited[a]=0
while q:
    now,cnt =q.popleft()
    for NEXT in graph[now]:
        if visited[NEXT]>cnt+1:
            visited[NEXT]=cnt+1
            q.append([NEXT,cnt+1])

if visited[b]==INF:
    print(-1)
else:
    print(visited[b])