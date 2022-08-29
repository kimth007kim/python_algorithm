def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    time = 0
    print(alp, cop)
    for a, b, c, d, e in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)

    start_alp = min(alp, max_alp)
    start_cop = min(cop, max_cop)
    inf = int(1e9)
    dp = [[inf] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[start_alp][start_cop] = 0
    for i in range(start_alp, max_alp + 1):
        for j in range(start_cop, max_cop + 1):
            # if i==start_alp+1 and  j== start_cop+1:
            #     continue
            dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j])
            for a, b, c, d, e in problems:
                if i - a >= 0 and j - b >= 0 and i - c >= 0 and j - d >= 0:
                    if dp[i - c][j - d] > 0:
                        dp[i][j] = min(dp[i - c][j - d] + e, dp[i][j])
    #         print(i,j)
    # for i in dp:
    #     print(i)

    # answer = 0
    return dp[-1][-1]