n= int(input())
arr= list(map(int,input().split()))

dp=[1]*n

for i in range(1,n):
    for j in range(i):
        print( "arr[{}]={} arr[{}]={}".format(i,arr[i],j,arr[j]))
        if arr[j]>arr[i]:
            dp[i]=max(dp[i],dp[j]+1)
            print(dp)