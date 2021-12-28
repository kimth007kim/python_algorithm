
n=int(input())
dp=[1000000]*(n+1)
dp[n]=0
for i in range(n,0,-1):
    if i-1>0:
        dp[i-1]=min(dp[i]+1,dp[i-1])

    if i%2==0 and i//2>0:
        dp[i//2]= min(dp[i]+1,dp[i//2])
    if i % 3 == 0 and i // 3 > 0:
        dp[i // 3] = min(dp[i] + 1, dp[i // 3])

print(dp[1])