from collections import deque
import sys

input =sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [10000] * (n + 1)
answer=0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append([1,0])
visited[1]=0

while q:
    now,cnt = q.popleft()
    for i in graph[now]:
        if visited[i]>cnt+1:
            visited[i]=cnt+1
            q.append([i,cnt+1])
        # print(i)

for i in range(1,n+1):
    if visited[i]>=1 and visited[i]<=2:
        answer+=1

print(answer)