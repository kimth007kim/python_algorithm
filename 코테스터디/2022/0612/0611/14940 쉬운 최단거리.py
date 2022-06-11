from collections import deque
import sys

input =sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = []
visited = [[0] * m for _ in range(n)]
sx = 0
sy = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            sx = i
            sy = j
    arr.append(tmp)
q = deque()
q.append([sx, sy, 0])
while q:
    x,y,cnt =q.popleft()
    if visited[x][y]==0:
        visited[x][y]=cnt
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==1 and visited[nx][ny]==0 or visited[nx][ny]>cnt+1:
                visited[nx][ny]=cnt+1
                q.append([nx,ny,cnt+1])



for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and arr[i][j]==1:
            visited[i][j]=-1

for i in visited:
    print(*i)