from collections import deque,defaultdict
import sys

input =sys.stdin.readline



n,m = map(int,input().split())
# print(n,m)

point=defaultdict(list)
graph=  [ [] for _ in range(n+1)]

visited=[False] *(n+1)
# print(graph)
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

MAX=0
q=deque()
q.append([1,0])
visited[1]=True
while q:
    now,cnt= q.popleft()
    MAX=max(MAX,cnt)
    for i in graph[now]:
        if visited[i]==False:
            q.append([i,cnt+1])
            visited[i]=True
            point[cnt+1].append(i)

answer=  min(point[MAX])
length = len(point[MAX])

print(answer,MAX,length)