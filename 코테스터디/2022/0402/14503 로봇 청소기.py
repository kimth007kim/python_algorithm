from collections import deque
import sys

input = sys.stdin.readline
n,m= map(int,input().split())
x,y,d= map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            visited[i][j]=-1

q=deque()
q.append([1,x,y,d])
visited[x][y]=1
while q:
    cnt,x,y,d=q.popleft()
    for i in range(4):
        d= (d+4-1)%4
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny]==0:
                visited[nx][ny]=cnt+1
                q.append([cnt+1,nx,ny,d])
                break
    else:
        next =(d+4-2)%4
        nx=x+dx[next]
        ny=y+dy[next]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny]==0:
                visited[nx][ny] = cnt + 1
                q.append([cnt + 1, nx, ny, d])
            elif visited[nx][ny]!=-1 and visited[nx][ny]!=0:
                q.append([cnt,nx,ny,d])
print(cnt)