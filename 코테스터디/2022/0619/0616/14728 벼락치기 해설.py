n,t = map(int,input().split())
time, score = [], []

for i in range(n):
    K, S = map(int, input().split())
    time.append(K)
    score.append(S)

print(time,score)

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,t+1):
        if j>= time[i-1]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-time[i-1]]+score[i-1])
        else:
            dp[i][j]=dp[i-1][j]

        for k in dp:
            print(k)

print(dp[n][t])