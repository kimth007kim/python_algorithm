import sys

input =sys.stdin.readline

n= int(input())
# n= 800
arr= list(map(int,input().split()))

# print(arr)
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i]=arr[i-1]
    for j in range(1,i//2+1):
        dp[i]=max(dp[i],dp[i-j]+dp[j])

print(dp[n])