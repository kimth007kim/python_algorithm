
import sys
input = sys.stdin.readline


n= int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

dp = [0]*(n+1)
dp[1]=arr[0]
if n>1:
    dp[2]=arr[1]+arr[0]
for i in range(3,n+1):
    print(arr[i-2],arr[i-3],dp[i-4],"   ",arr[i-1],dp[i-2])
    dp[i]= max(dp[i-1],dp[i-3]+arr[i-2]+arr[i-1],arr[i-1]+dp[i-2])
print(dp)
print(dp[n])