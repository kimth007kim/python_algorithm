import sys

input =sys.stdin.readline


n = int(input())
arr = []
size = -1
for i in range(n):
    t = int(input())
    size = max(size, t)
    arr.append(t)

if size < 5:
    dp = [0] * (5 + 1)
else:
    dp = [0] * (size + 1)

dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2

for i in range(6,size+1):
    dp[i]=dp[i-1]+dp[i-5]

for i in arr:
    print(dp[i])