import sys

input =sys.stdin.readline


t= int(input())
for _ in range(t):
    n= int(input())
    arr=[]
    dp=[[0]*(n+1) for _ in range(2)]
    arr.append(list(map(int,input().split())))
    arr.append(list(map(int,input().split())))

    dp[0][1]=arr[0][0]
    dp[1][1]=arr[1][0]
    for j in range(2,n+1):
        for i in range(2):
            if i==0:
                dp[i][j]+=max(arr[i][j-1]+dp[1][j-1], arr[i][j-1]+dp[1][j-2],arr[i][j-1]+dp[0][j-2])
            else:
                dp[i][j]+=max(arr[i][j-1]+dp[0][j-1], arr[i][j-1]+dp[1][j-2],arr[i][j-1]+dp[0][j-2])
    print(max(dp[0][n],dp[1][n]))