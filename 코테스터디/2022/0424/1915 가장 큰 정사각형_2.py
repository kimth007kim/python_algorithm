n,m = map(int,input().split())
board = [list(map(int,list(input())))for _ in range(n)]


dp=[[0]*(m+1)for _ in range(n+1)]
side=0

for i in range(1,n+1):
    for j in range(1,m+1):
        # print(i,j, board[i-1][j-1])
        if board[i-1][j-1]==1:
            dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
            if side<dp[i][j]:
                side=dp[i][j]

print(side**2)