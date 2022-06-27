import sys
input =sys.stdin.readline


n = int(input())

dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(3)]
arr = []
for i in range(1, n + 1):
    arr.append(list(map(int, input().split())))

dp[0][1][2] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for a in range(3):
            if arr[i - 1][j - 1] == 1:
                continue
            if a == 0:
                # if j + 1 <= n and arr[i - 1][j] != 1:

                # if arr[i-1][j-1]!=1
                dp[a][i][j] += dp[0][i][j - 1] + dp[1][i][j - 1]
            elif a == 1:
                # if i + 1 <= n and j + 1 <= n and arr[i - 1][j - 1] != 1:
                if arr[i-2][j-1]==0 and arr[i-1][j-2]==0:
                    dp[a][i][j]+=dp[0][i-1][j-1]+dp[2][i-1][j-1]+dp[1][i - 1][j - 1]
                #
                #     dp[a][i][j]+=
                # dp[a][i][j] +=
            else:
                # if i + 1 <= n and arr[i][j-1] != 1:
                dp[a][i][j] += dp[1][i - 1][j] + dp[2][i - 1][j]
answer=0
for i in range(3):
    answer+=dp[i][n][n]

print(answer)