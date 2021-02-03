from collections import deque

def bfs():
    q=deque()
    q.append((sx,sy))
    while q:
        x,y= q.popleft()
        if x== ex and y == ey:
            return visited[x][y]
        for i in range(8):
            nx= x+dx[i]
            ny= y +dy[i]
            if nx<0 or ny<0 or nx>=l or ny>=l:
                continue
            if not visited[nx][ny]:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))

dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,1,-1]
ans=[]
case = int(input())
for _ in range(case):
    l= int(input())
    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())
    visited= [[0]* l for _ in range(l)]
    ans.append(bfs())

for j in ans:
    print(j)