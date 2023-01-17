n,m = map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        tmp = 0
        if graph[i-1][j-1]==1:
            tmp=1
        dp[i][j]=tmp+max(dp[i][j-1],dp[i-1][j])

print(dp[n][m])