import sys

input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

dp=[1 for _ in range(n+1)]
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            print(i,j)
            dp[i]=max(dp[i],dp[j]+1)
            print(dp)
