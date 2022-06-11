t= int(input())
for i in range(t):
    n= int(input())
    arr= list(map(int,input().split()))
    dp=[0]*(n+1)

    for j in range(1,n+1):
        dp[j]= max(arr[j-1],dp[j-1]+arr[j-1])
        # print(dp)
    MAX =max(dp[1:])

    print(MAX)
    # break