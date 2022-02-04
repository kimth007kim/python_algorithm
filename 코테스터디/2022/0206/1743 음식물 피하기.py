def show(graph):
    for i in graph:
        print(i)
    print()

dx= [1,0,-1,0]
dy= [0,1,0,-1]

def dfs(x,y):
    visited[x][y]=1
    global cnt
    cnt+=1
    for i in range(4):
        nx = dx[i]+x
        ny= dy[i]+y
        if 0<=nx<=n-1 and 0<=ny<=m-1:
            if visited[nx][ny]==0 and graph[nx][ny]==1:
                dfs(nx,ny)

n,m,k= map(int,input().split())

graph= [ [0]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]

for i in range(k):
    x,y= map(int,input().split())
    graph[x-1][y-1]=1

_max=0
for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and graph[i][j]==1:
            cnt=0
            dfs(i,j)
            _max= max(_max,cnt)
print(_max)