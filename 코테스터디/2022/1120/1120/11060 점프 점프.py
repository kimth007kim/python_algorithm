import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
INF = int(1e11)
dp = [INF] * (n)
dp[0] = 0
for i in range(n):
    if arr[i] == 0:
        continue
    for j in range(1, arr[i] + 1):
        if i + j >= n:
            break
        dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n-1]==INF:
    print(-1)
else:
    print(dp[n - 1])
