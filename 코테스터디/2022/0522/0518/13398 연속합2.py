n= int(input())
arr= list(map(int,input().split()))


print(n)
print(arr)

dp =[[0]* (n+1) for _ in range(n+1)]

dp = [ [0]*n for _ in range(2)]
dp[0][0]= arr[0]
ans=-1e9
if n>1:
    for i in range(1,n):
        dp[0][i]= max(dp[0][i-1]+arr[i],arr[i])
        print(dp[0][i-1],dp[1][i-1]+arr[i])
        dp[1][i]=max(dp[0][i-1],dp[1][i-1]+arr[i])

        ans = max(ans,dp[0][i],dp[1][i])
    print(ans)
else:
    print(dp[0][0])