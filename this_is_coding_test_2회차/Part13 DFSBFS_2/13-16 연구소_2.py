n,m= map(int,input().split())
temp=[[0]*(m) for _ in range(n)]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

max_Value=0

def virus(x,y):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

def cscore():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

def dfs(cnt):
    global max_Value
    if cnt==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        max_Value=max(max_Value,cscore())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                dfs(cnt+1)
                graph[i][j]=0

dfs(0)
print(max_Value)