n,m= map(int,input().split())
array= list(map(int,input().split()))

dp = []
index=0
for i in range(n):
    dp.append(array[index:index+m])
    index+=m
print(dp)

for j in range(1,m):
    for i in range(n):
        if i == 0:
            left_top=0
        else:
            left_top=dp[i-1][j-1]
        if i == n-1:
            left_down=0
        else:
            left_down=dp[i+1][j-1]
        left = dp[i][j-1]
        dp[i][j]+=max(left_down,left,left_top)

answer=0
for i in range(n):
    answer=max(answer,dp[i][m-1])

print(answer)