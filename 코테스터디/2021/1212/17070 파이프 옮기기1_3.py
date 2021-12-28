def SHOW(dp):
    for i in dp:
        for j in i:
            print(j)
        print()


n= int(input())
arr=[ list(map(int,input().split())) for _ in range(n)]

dp=[[[0]*n for _ in range(n)] for _ in range(3)]

print(dp)

for i in range(1,n):
    if arr[0][i]==1:
        break
    dp[0][0][i]=1

for i in range(1,n):
    for j in range(2,n):
        if arr[i][j-1]==0 and arr[i-1][j-1]==0 and arr[i-1][j]==0:
            dp[2][i][j]= sum(dp[k][i-1][j-1] for k in range(3))
        if arr[i][j]==0:
            dp[0][i][j]=dp[0][i][j-1]+dp[2][i][j-1]
            dp[1][i][j]=dp[1][i-1][j]+dp[2][i-1][j]

print(sum(dp[k][-1][-1] for k in range(3)))