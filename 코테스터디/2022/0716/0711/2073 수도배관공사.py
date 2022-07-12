d, p = map(int, input().split())

INF = int(1e9)
dp = [[0]*(d+1) for _ in range(p+1)]

pipe = []
for i in range(p):
    a,b = map(int,input().split())
    pipe.append([a,b])

for i in range(1,p+1):
    for j in range(1,d+1):
        a=1
        if (j-pipe[i-1][0])>=0 and dp[i-1][j-pipe[i-1][0]] !=0:
            dp[i][j]=min(dp[i-1][j-pipe[i-1][0]],pipe[i-1][1])
        dp[i][j]=max(dp[i][j],dp[i-1][j])
            # print(j,i,i-1,pipe[i-1][0])
            # dp[i][j]=min(dp[i-1][j],dp[i][j-pipe[j-1][0]])
            # print(j,pipe[j-1][0],j-pipe[j-1][0])
    if pipe[i-1][0]<=d:
        dp[i][pipe[i-1][0]]=max(dp[i][pipe[i-1][0]],pipe[i-1][1])

print(dp[p][d])