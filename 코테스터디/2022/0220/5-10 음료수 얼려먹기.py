n,m = map(int,input().split())

graph=[]
for i in range(n):
    tmp= list(map(int,list(input())))
    graph.append(tmp)

dx=[1,0,-1,0]
dy=[0,1,0,-1]
# visited=[[False]*m for i in range(n)]

def dfs(graph,x,y):
    graph[x][y]=1
    for i in range(4):
        nx= dx[i]+x
        ny= dy[i]+y
        if 0<=nx<n and 0 <= ny <m:
            if graph[nx][ny]==0:
                dfs(graph,nx,ny)




cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(i,j)
            dfs(graph,i,j)
            cnt+=1

print(cnt)
