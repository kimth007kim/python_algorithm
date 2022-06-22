t= int(input())
arr=[]
for i in range(t):
    arr.append(int(input()))

MAX= max(arr)
dp = [[0]*11 for _ in range(MAX+1)]
for i in range(1,11):
    dp[1][i]=1

for i in range(2,MAX+1):
    for j in range(1,11):
        dp[i][j]= dp[i-1][j]+dp[i][j-1]

for i in arr:
    print(sum(dp[i]))