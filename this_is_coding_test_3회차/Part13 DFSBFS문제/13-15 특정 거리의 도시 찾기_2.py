from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)
n,m,target,start= map(int,input().split())

visited= [False]* n

graph=[[]*(n+1) for _ in range(n+1)]
distance= [INF]*(n+1)
#
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)


q=deque([start])
distance[start]=0
while q:
    now =q.popleft()
    for i in graph[now]:
        if distance[i]== INF:
            distance[i]= distance[now]+1
            q.append(i)
answer=[]
for i in range(len(distance)):
    if distance[i] == target:
        answer.append(i)

if not answer:
    print(-1)
else:
    for i in answer:
        print(i)
