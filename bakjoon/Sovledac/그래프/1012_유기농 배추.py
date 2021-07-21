import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

t= int(input())
answer=[]

for i in range(t):
    m,n,k= map(int,input().split())

    # m=5
    # n=3

    graph= [[0]*m for _ in range(n)]
    for i in range(k):
        x,y= map(int,input().split())
        graph[y][x]=1

    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    def dfs(x,y):
        if x<0 or y<0 or x>=n or y>=m:
            return False
        if graph[x][y]==0:
            return False
        graph[x][y] = 0
        # for i in range(4):
        #     nx= dx[i]+x
        #     ny= dy[i]+y
        #     if nx>=0 and ny>=0 and nx<n and ny<m and graph[nx][ny]==1:
        #         dfs(nx,ny)
        #         return True
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    cnt=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==1:
                cnt+=1
    answer.append(cnt)

for j in answer:
    print(j)