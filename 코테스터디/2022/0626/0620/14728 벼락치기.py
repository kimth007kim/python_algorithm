n,t = map(int,input().split())
time=[]
score=[]
for _ in range(n):
    a,b =map(int,input().split())
    time.append(a)
    score.append(b)

dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,t+1):
        if time[i-1]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-time[i-1]]+score[i-1])
            # continue
        else:
            dp[i][j]=dp[i-1][j]
            # print(i,j)
        # print(i,j)
        # for k in dp:
        #     print(k)

print(dp[n][t])