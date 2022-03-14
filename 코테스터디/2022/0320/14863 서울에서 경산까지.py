n,k=map(int,input().split())
trip=[]
dp = [[-1]*100 for _ in range(n+1)]
for i in range(n):
    trip.append(list(map(int,input().split())))

dp[0][trip[0][0]]=trip[0][1]
dp[0][trip[0][2]]=trip[0][3]

result =0

for i in range(1,n):
    for j in range(k+1):
        if dp[i-1][j]== -1:
            continue
        if (j+trip[i][0])<=k:
            dp[i][j+trip[i][0]]=max(dp[i][j+trip[i][0]],dp[i-1][j]+trip[i][1])
            result = max(result,dp[i][j+trip[i][0]])
        if(j+trip[i][2])<=k:
            dp[i][j+trip[i][2]]=max(dp[i][j+trip[i][2]],dp[i-1][j]+trip[i][3])
            result = max(result, dp[i][j + trip[i][2]])
    for a in dp:
        print(a)
    print()

for a in dp:
    print(a)
print()

print(result)
