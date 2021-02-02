from collections import deque

def bfs():
    q=deque()
    q.append((s_x,s_y))
    while q:
        x,y= q.popleft()
        if x == e_x and y == e_y:
            return visited[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx>=l or ny<0 or ny>=l:
                continue
            if not visited[nx][ny]:
                visited[nx][ny]= visited[x][y]+1
                q.append((nx,ny))

dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,1,-1]
case =int(input())
for i in range(case):
    l=int(input())
    visited= [[0]* l for i in range(l)]
    s_x,s_y=map(int,input().split())
    e_x,e_y=map(int,input().split())
    print(bfs())