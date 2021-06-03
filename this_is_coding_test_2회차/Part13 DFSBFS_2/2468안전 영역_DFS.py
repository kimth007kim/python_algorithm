import sys
sys.setrecursionlimit(10**7)
n= int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
graph= []

start=-1
for i in range(n):
    tmp =list(map(int,input().split()))
    for j in range(n):
        start=max(tmp[j],start)
    graph.append(tmp)




def dfs(x,y,target):
    ngraph[x][y]=10001
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if ngraph[nx][ny] != 10001 and ngraph[nx][ny]>target:
                dfs(nx,ny,target)



max_value=0
for target in range(start,-1,-1):
    cnt=0
    ngraph=[[-1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ngraph[i][j]=graph[i][j]
    for i in range(n):
        for j in range(n):
            if ngraph[i][j]>target and ngraph[i][j] != 10001:
                dfs(i,j,target)
                cnt+=1
    max_value=max(cnt,max_value)

print(max_value)