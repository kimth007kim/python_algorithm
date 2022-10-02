n= int(input())
arr=[0]
for i in range(n):
    arr.append(int(input()))
for i in range(300-n):
    arr.append(0)
dp=[0]*(301)
dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
# print(arr)
# print(dp)
for i in range(3,n+1):
    dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])

print(dp[n])