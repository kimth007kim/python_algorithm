from collections import deque
ans=[]
dy=[0,0,-1,1]
dx=[-1,1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        y,x=q.popleft()
        graph[y][x]=0
        for i in range(4):
            ny = y+dy[i]
            nx= x+dx[i]
            if 0<= ny and ny<n and 0<nx and nx<m and graph[ny][nx]==1:
                q.append((x,y))
                graph[ny][nx]=0

    return 1


t= int(input())
for _ in range(t):
    m,n,v= map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    for i in range(v):
        x,y= map(int,input().split())
        graph[y][x]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[y][x]==1:
                print(cnt)
                print(bfs(y,x))
                cnt+=bfs(y,x)
    ans.append(cnt)
for j in ans:
    print(j)