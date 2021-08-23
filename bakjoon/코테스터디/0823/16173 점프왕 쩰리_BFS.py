import sys
from collections import deque
input= sys.stdin.readline

dx=[0,1]
dy=[1,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    while q:
        # print(q)
        x,y= q.popleft()
        visited[x][y] = True
        for i in range(2):
            nx= dx[i]*graph[x][y]+x
            ny= dy[i]*graph[x][y]+y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append((nx,ny))


n= int(input())
graph= []
for i in range(n):
    graph.append(list(map(int,input().split())))
visited=[[False]*n for _ in range(n)]


bfs(0,0)
if visited[n-1][n-1]:
    print("HaruHaru")
else:
    print("Hing")