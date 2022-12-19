from collections import deque
import sys

input = sys.stdin.readline
def enemy():
    for i in range(1, n + 1):
        if visited[i]==0:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                now = q.popleft()
                for j in graph[now]:
                    print(now,j)
                    if visited[j] == visited[now]:
                        return 0
                    if visited[j] == 0:
                        visited[j]= -visited[now]
                        q.append(j)
    return 1
n,m = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
print(enemy())