from collections import deque

t= int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    print(q)
    while q:
        a,b= q[-1][0],q[-1][1]
        y,x=q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or ny >=n or nx<0 or nx>=m:
                continue
            if graph[ny][nx]==1 and visited[ny][nx]==False:
                visited[ny][nx]=True
                q.append((ny,nx))
        return cnt

for i in range(t):
    m,n,k = map(int,input().split())
    visited = [[0] * m for j in range(n)]
    graph= [[False]*m for j in range(n)]


    for j in range(k):
        x,y= map(int,input().split())
        graph[y][x]=1

    ans=0
    for j in range(n):
        for k in range(m):
            if graph[j][k]== 1  and visited[j][k]==False:
                ans+=bfs(j,k)
    print(ans)