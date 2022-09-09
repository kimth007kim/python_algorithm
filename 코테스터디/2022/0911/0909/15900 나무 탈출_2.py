import sys
from collections import deque

input =sys.stdin.readline
n= int(input())

graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append([1,0])
visited= [False]*(n+1)
visited[1]=True
total=0
while q:
    now,cnt =q.popleft()
    if len(graph[now])==1 and now!=1:
        total+=cnt
        continue
    for i in graph[now]:
        if visited[i]==False:
            q.append([i,cnt+1])
            visited[i]=True

if total%2==0:
    print("No")
else:
    print("Yes")