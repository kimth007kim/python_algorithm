n= int(input())
data=list(map(int,input().split()))
dp=[1]*(n)
data.reverse()
# for i in range(len)
# print(d)
print(data)
for i in range(1,n):
    for j in range(0,i):
        print("i=",i,"  j=",j)
        print(data[i],"---",data[j])
        if data[j]<data[i]:
            dp[i]=max(dp[i],dp[j]+1)
            print("############바뀜",i,dp[i])
            print(dp)

print(dp)
print(n-max(dp))