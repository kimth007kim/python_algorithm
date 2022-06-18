n,t=map(int,input().split())
dp = [[0]*(t+1) for _ in range(n+1)]
for i in dp:
    print(i)

time =[]
score=[]
for i in range(n):
    k,s = map(int,input().split())
    time.append(k)
    score.append(s)

for i in range(1,n+1):
    for j in range(1,t+1):
        if time[i-1]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-time[i-1]]+score[i-1])
        else:
            dp[i][j]=dp[i-1][j]

        for k in dp:
            print(k)