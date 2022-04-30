import sys

input = sys.stdin.readline

n = int(input())
# min_dp = [[0] * 3 for _ in range(n + 1)]
# max_dp = [[0] * 3 for _ in range(n + 1)]

min_dp=[0]*3
max_dp=[0]*3

min_next=[0]*3
max_next=[0]*3
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))



for i in range(3):
    min_dp[i] = arr[0][i]
    max_dp[i] = arr[0][i]



for i in range(2, n + 1):
    for j in range(3):
        if j == 0:
            max_next[j] = arr[i - 1][j] + max(max_dp[j], max_dp[j + 1])
            min_next[j] = arr[i - 1][j] + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_next[j] = arr[i - 1][j] + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_next[j] = arr[i - 1][j] + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_next[j] = arr[i - 1][j] + max(max_dp[j - 1], max_dp[j])
            min_next[j] = arr[i - 1][j] + min(min_dp[j - 1], min_dp[j])


    for j in range(3):
        min_dp[j]=min_next[j]
        max_dp[j]=max_next[j]

print(max(max_dp),min(min_dp))