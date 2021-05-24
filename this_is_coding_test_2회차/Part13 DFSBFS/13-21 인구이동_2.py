from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

n,l,r=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


def bfs(x,y,index):
    united=[]
    united.append((x,y))
    cnt=1
    q= deque()
    q.append((x,y))
    summary=graph[x][y]
    union[x][y]=index
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(graph[nx][ny]- graph[x][y])<=r:
                    q.append((nx,ny))
                    union[nx][ny]=index
                    summary+=graph[nx][ny]
                    united.append((nx,ny))
                    cnt+=1

    for x,y in united:
        graph[x][y]=summary//cnt
    print(graph)

total=0

while True:
    union = [[-1]*n for _ in range(n)]
    index=0

    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                bfs(i,j,index)
                index+=1
    if index==n*n:
        break
    total+=1

print(total)