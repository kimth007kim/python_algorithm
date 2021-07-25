def bfs(x,y):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if (0<=nx<n) and (0<=ny<m):
            if graph[nx][ny]=="S":
                return False
            if graph[nx][ny]==".":
                graph[nx][ny]="D"
    return True


n,m=map(int,input().split())
graph=[list(input()) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

for i in range(n):
    for j in range(m):
        t =True
        if graph[i][j]=="W":
            t= bfs(i,j)
            if t== False:
                print(0)
                break
if t:
    print(1)
    for i in graph:
        print("".join(i))