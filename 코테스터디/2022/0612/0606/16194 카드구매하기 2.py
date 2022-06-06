import sys

input = sys.stdin.readline
n= int(input())
arr= list(map(int,input().split()))

dp = [1e11]*(n+1)
dp[0]=0


for i in range(1,n+1):
    for j in range(len(arr)):
        if i-j-1>=0 and i-j-1<n+1:
            dp[i]=min(dp[i],dp[i-j-1]+arr[j])
print(dp[n])