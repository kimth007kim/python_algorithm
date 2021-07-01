from collections import deque

def solution(maps):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    # show(maps)
    n=len(maps)
    m=len(maps[0])
    visited=[[0]*m for _ in range(n)]

    q= deque()
    q.append((0,0))
    dist=1
    visited[0][0]=dist
    while q:
        x,y =q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))

    if visited[n-1][m-1]==0:
        return -1
    else:
        return visited[n-1][m-1]


def show(maps):
    for i in maps:
        print(i)