n= int(input())
arr = list(map(int,input().split()))

dp = [1]*(n+1)

for i in range(2,n+1):
    for j in range(1,i):
        if arr[i-1]>arr[j-1]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))