import sys
from collections import deque
input=sys.stdin.readline
INF= int(1e9)

# n,m,k,x=4,4,2,1
# data=[[1,2],[1,3],[2,3],[2,4]]


n,m,k,x= map(int,input().split())
visited=[False]*(n+1)
data=[]
graph=[[] for _ in range(n+1)]
# print(graph)
for i in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)


distance=[INF]*(n+1)
q=deque()
q.append(x)
visited[x]=True
distance[x]=0
while q:
    dist=q.popleft()
    for i in graph[dist]:
        if visited[i]==False:
            distance[i]=min(distance[i],distance[dist]+1)
            visited[i]=True
        # print(distance)
            q.append(i)

# print(visited)
result=[]
for i in range(len(distance)):
    if distance[i]==k:
        result.append(i)
# print(result)
# print(distance)

if len(result)==0:
    print(-1)
else:
    for r in result:
        print(r)
