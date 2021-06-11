n= int(input())
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(dp[i])):
        if j==0:
            left=0
        else:
            left = dp[i-1][j-1]
        if i ==j:
            right=0
        else:
            right=dp[i-1][j]
        dp[i][j]+=max(left,right)
result=0
for i in range(n):
    result=max(result,dp[n-1][i])
print(result)