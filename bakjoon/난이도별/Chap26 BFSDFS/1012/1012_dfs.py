# 런타임 에러발생

import sys
sys.setrecursionlimit(10000)

t= int(input())
ans=[]
for i in range(t):
    m,n,k= map(int,input().split())
    graph=[[0]*m for i in range(n)]


    for k in range(k):
        x,y= map(int,input().split())
        graph[y][x]=1

    def dfs(y,x):
        cnt=0
        if x <0 or x>=m or y<0 or y>=n:
            return False
        if graph[y][x]==1:
            graph[y][x]=0
            cnt+=1
            dfs(y-1,x)
            dfs(y,x-1)
            dfs(y+1,x)
            dfs(y,x+1)
            return True
        return False

    result=0
    for y in range(n):
        for x in range(m):
            if dfs(y,x)==1:
                result+=1

    ans.append(result)

for i in ans:
    print(i)
