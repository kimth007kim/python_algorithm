# n,k= map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))
n,k=3,10
arr=[1,2,5]

dp=[0]*11

dp[0]=1

for i in arr:
    for j in range(1,k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]
            print(i,j,dp)