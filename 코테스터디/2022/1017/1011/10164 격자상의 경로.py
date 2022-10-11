n, m, k = map(int, input().split())

dp = [[0] * (m) for _ in range(n)]
dp[0][0]=1
if k ==0:

    for i in range(n):
        for j in range(m):
            if j-1>=0:
                dp[i][j]+=dp[i][j-1]
            if i-1>=0:
                dp[i][j]+=dp[i-1][j]
else:
    x, y = (k - 1) // m, (k - 1) % m
    for i in range(x+1):
        for j in range(y+1):
            if j-1>=0:
                dp[i][j]+=dp[i][j-1]
            if i-1>=0:
                dp[i][j]+=dp[i-1][j]
    for i in range(x,n):
        for j in range(y,m):
            if i==x and j==y:
                continue
            if j-1>=0:
                dp[i][j]+=dp[i][j-1]
            if i-1>=0:
                dp[i][j]+=dp[i-1][j]

print(dp[n-1][m-1])
