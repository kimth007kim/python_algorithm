from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    tmp = list(map(int, list(input())))
    arr.append(tmp)
INF= int(1e9)
visited = [[[INF] * (m) for _ in range(n)] for _ in range(2)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

if arr[0][0] == 0:
    visited[0][0][0] = 1

q = deque()
q.append([0, 0, visited[0][0][0],0])
while q:
    x, y, cnt, wall = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==0:
                if wall==0 and visited[0][nx][ny]==INF:
                    visited[0][nx][ny]=cnt+1
                    q.append([nx,ny,cnt+1,0])
                if wall==1 and visited[1][nx][ny]==INF:
                    visited[1][nx][ny]=cnt+1
                    q.append([nx,ny,cnt+1,1])

            if arr[nx][ny]==1 and wall==0 and visited[1][nx][ny]==INF:
                visited[1][nx][ny]=cnt+1
                q.append([nx,ny,cnt+1,1])

answer = min(visited[0][n-1][m-1],visited[1][n-1][m-1])
if answer == INF:
    print(-1)
else:
    print(answer)