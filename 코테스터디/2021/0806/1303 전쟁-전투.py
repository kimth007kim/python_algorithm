from collections import deque
import sys

input=sys.stdin.readline

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y,team):
    cnt=1
    q=deque()
    q.append((x,y,team))
    visited[x][y]=True

    while q:
        x,y,team=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==team and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny,team))
                    cnt+=1

    return cnt**2

n,m = map(int,input().split())
visited= [[False]*n for _ in range(m)]
graph=[]
for i in range(m):
    graph.append(list(input().strip()))



Bcnt=0
Wcnt=0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j]=="W":
                Wcnt+=bfs(i, j, graph[i][j])
            else:
                Bcnt+=bfs(i,j,graph[i][j])

print(Wcnt,Bcnt)