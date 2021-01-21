from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y +dy[i]
            # if nx<0 or nx>=n or ny<0 or ny>=m:
            #     continue
            # if graph[nx][ny]==0:
            #     continue

            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
            # if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]



n,m= map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]


print(bfs(0,0))