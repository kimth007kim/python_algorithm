n=int(input())
dp=[]

for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        # print(i,j)
        if j==0:
            up_left=0
        else:
            up_left=dp[i-1][j-1]
        if j==i:
            up=0
        else:
            up=dp[i-1][j]
        print(dp[i][j],up_left,up,max(up_left,up))
        dp[i][j]=dp[i][j]+max(up_left,up)



print(max(dp[n-1]))