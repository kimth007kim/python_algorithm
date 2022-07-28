import sys

input =sys.stdin.readline

n, k = map(int, input().split())
# n 물품수
# k 배낭한계
dp = [[0] * (k + 1) for _ in range(n + 1)]
back = []
for i in range(n):
    weight, value = map(int, input().split())
    back.append([weight, value])

# for i in dp:
#     print(i)


for i in range(1, n + 1):
    w, v = back[i - 1]
    # print(w,v)
    for j in range(1, k + 1):
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j ], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

for i in dp:
    print(i)
print(dp[n][k])