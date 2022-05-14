def solution():
    n,k= map(int,input().split())
    satisfactions = [0]+list(map(int,input().split()))
    # print(n,k)
    # print(satisfactions)
    left,right=1,1
    sum=0
    dp = [0]*(n+1)

    while left<=n and right<=n:
        if sum>=k:
            sum-=satisfactions[left]
            left+=1
            # print("sum>=k",sum,">=",k,left,right)
        else:
            sum+=satisfactions[right]
            # print("dp[right-1]",dp[right-1],"dp[left-1]+sum-k",dp[left-1]+sum-k)
            dp[right]=max(dp[right-1],dp[left-1]+sum-k)
            right+=1
            # print("sum<k",sum,"<",k,left,right)

        # print(dp)
        # print()
print(solution())