wordA=list(input())
wordB=list(input())

dp =[[0]* (len(wordB)+1) for _ in range(len(wordA)+1)]


for i in range(1,len(wordA)+1):
    for j in range(1,len(wordB)+1):
        if wordA[i-1]!=wordB[j-1]:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j]=dp[i-1][j-1]+1

print(dp[-1][-1])
