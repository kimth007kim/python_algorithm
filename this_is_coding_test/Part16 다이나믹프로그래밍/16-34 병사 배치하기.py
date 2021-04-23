n= int(input())
array=list(map(int,input().split()))
array.reverse()

print(array)
dp=[1]*n


for i in range(1,n):
    for j in range(0,i):
        print("i",i,"j",j,array[i],array[j])
        if array[j]<array[i]:
            # print(dp[i],dp[j]+1)
            dp[i]=max(dp[i],dp[j]+1)

print(dp)
print(n-max(dp))