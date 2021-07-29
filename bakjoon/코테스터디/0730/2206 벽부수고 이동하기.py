import sys
from collections import deque

input=sys.stdin.readline
INF=int(1e9)

n,m= map(int,input().split())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def copydata(data):
    graph=[[0]*(m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph[i][j] = data[i][j]
    return graph

def bfs(graph):

    visited = [[INF] * (m) for _ in range(n)]
    q=deque()
    x,y,dist=0,0,1
    q.append((x,y,dist))
    visited[x][y]=dist
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<m and visited[nx][ny]==INF and graph[nx][ny]==0:
                visited[nx][ny]=dist+1
                q.append((nx,ny,dist+1))


    return visited[n-1][m-1]


data=[]
for i in range(n):
    data.append(list(map(int,input().rstrip())))


result=[]

wall = []
for i in range(n):
    for j in range(m):
        if data[i][j]==1:
            wall.append((i,j))



normal=copydata(data)
MIN=(bfs(normal))



for x,y in wall:
    graph=copydata(data)
    graph[x][y]=0
    tmp=bfs(graph)
    MIN=min(MIN,tmp)

if MIN==INF:
    print(-1)
else:
    print(MIN)