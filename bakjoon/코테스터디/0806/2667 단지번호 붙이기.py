import sys
from collections import deque
input = sys.stdin.readline


dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    cnt=1
    q= deque()
    visited[x][y]=True
    graph[x][y]=0
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
                graph[nx][ny]=0
                cnt+=1
    return cnt

n= int(input())

data=[list(input().strip()) for _ in range(n)]
graph= [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j]=int(data[i][j])

visited= [[False]*n for _ in range(n)]


result=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            cnt=bfs(i,j)
            result.append(cnt)


result.sort()
print(len(result))
for i in result:
    print(i)


