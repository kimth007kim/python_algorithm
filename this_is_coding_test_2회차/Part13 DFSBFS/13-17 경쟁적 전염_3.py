from collections import deque

n,k = map(int,input().split())

dx=[1,0,-1,0]
dy=[0,1,0,-1]

graph=[]
data=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))


data.sort()
q=deque(data)

es,ex,ey=map(int,input().split())



while q:
    v,s,x,y=q.popleft()
    if s==es:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny >=0 and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=v
                q.append((v,s+1,nx,ny))

print(graph[ex-1][ey-1])
