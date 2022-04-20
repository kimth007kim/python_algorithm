import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,m= map(int,input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[-1] * m for i in range(n)]

def dfs(x,y):
    if x==0 and y==0:
        return 1
    if dp[x][y]==-1:
        dp[x][y]=0

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[x][y]<arr[nx][ny]:
                    dp[x][y]+=dfs(nx,ny)
    for k in dp:
        print(k)
    print()
    return dp[x][y]
print(dfs(n-1,m-1))

for k in dp:
    print(k)
print()