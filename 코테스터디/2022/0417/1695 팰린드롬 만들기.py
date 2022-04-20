n=int(input())
arr= list(map(int,input().split()))

dp = [[0]*(n+1) for i in range(n+1)]
print(dp)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j)
        if arr[-i]==arr[j-1]:
            print("끝과 같다")
            print("arr[-i= {}]={} arr[j-1={}]={}".format(-i,j-1,arr[-1],arr[j-1]))
            # print(arr)
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        for k in dp:
            print(k)
print(n-dp[n][n])