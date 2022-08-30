def solution(alp, cop, problems):
    INF = int(1e9)
    max_alp = 0
    max_cop = 0
    for a, b, c, d, e in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)

    minAlp = min(max_alp, alp)
    minCop = min(max_cop, cop)
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[minAlp][minCop] = 0
    for i in range(minAlp, max_alp + 1):
        for j in range(minCop, max_cop + 1):
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            for a, b, c, d, e in problems:
                if i >= a and j >= b:
                    nx = min(i + c, max_alp)
                    ny = min(j + d, max_cop)
                    dp[nx][ny] = min(dp[nx][ny], dp[i][j] + e)

    return dp[-1][-1]