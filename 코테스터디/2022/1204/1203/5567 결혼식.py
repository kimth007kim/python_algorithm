n= int(input())

dp=[1]*(n+1)
dp[0]=0
arr= list(map(int,input().split()))

# print(arr)
for i in range(1,n+1):
    for j in range(1,i):
        # print(i,j,"  --  ",arr[i-1],arr[j-1])
        if arr[j-1]>arr[i-1]:
            dp[i]=max(dp[i],dp[j]+1)
# print(dp)
print(n-max(dp))