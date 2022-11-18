import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

a = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
dp[1] = k

for i in range(2, n + 1):
    min_v = max_v = a[i]
    print(min_v, max_v)
    dp[i] = dp[i - 1] + k
    for siz in range(2, min(m, i) + 1):
        j = i - siz + 1
        print(j)
        min_v, max_v = min(min_v, a[j]), max(max_v, a[j])
        box_cost = k + siz * (max_v + min_v)
        dp[i] = min(dp[i], dp[j - 1] + box_cost)
        print(min_v, max_v)
        print(dp)
print(dp[n])
