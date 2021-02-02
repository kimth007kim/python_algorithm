from sys import stdin
from collections import deque

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)

def bfs():
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            # print(d[x][y])
            # return
            return d[x][y]
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not d[nx][ny]:
                # print(nx,ny,d[nx][ny])
                for j in d:
                    print(j)
                print()
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
ans=[]
for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    d = [[0]*n for _ in range(n)]
    if sx== ex and sy==ey:
        ans.append(0)
    else:
        ans.append(bfs())

for j in ans:
    print(j)