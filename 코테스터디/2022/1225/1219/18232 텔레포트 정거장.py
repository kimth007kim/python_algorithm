from collections import deque
INF=int(1e11)
d= [1,-1]
n, m = map(int, input().split())
s, e = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[INF]*(n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)

q=deque()
q.append([s,0])
visited[s]=0

while q:
    now, cnt = q.popleft()
    for i in d:
        nx = i+now
        if 0<nx<=n:
            if visited[nx]>cnt+1:
                q.append([nx,cnt+1])
                visited[nx]=cnt+1
    for i in graph[now]:
        if visited[i] > cnt + 1:
            q.append([i, cnt + 1])
            visited[i] = cnt + 1


print(visited[e])