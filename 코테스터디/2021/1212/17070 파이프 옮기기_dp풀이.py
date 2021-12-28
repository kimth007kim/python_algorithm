import sys
from collections import deque

def SHOW(dp):
    print("---시작 ---")
    for i in dp:
        for j in i:
            print(j)
        print()
    print("---끝----")

input = sys.stdin.readline

n= int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp= [[[0]*n for _ in range(n)] for _ in range(3)]

dp[0][0][1]=1
i=2
while i<n:
    if arr[0][i]:
        print(arr[0][i])
        break
    dp[0][0][i]=1
    SHOW(dp)
    print()
    i+=1
print("---------------")
SHOW(dp)
print("---------------")
for i in range(1,n):
    for j in range(2,n):
        print(i,j)
        if arr[i][j]==0 and arr[i][j-1]==0 and arr[i-1][j]==0:
            dp[2][i][j]= sum(dp[k][i-1][j-1] for k in range(3))
            print("1번케이스")
            SHOW(dp)
        if arr[i][j]==0:
            dp[0][i][j]=dp[0][i][j-1]+dp[2][i][j-1]
            dp[1][i][j]=dp[1][i-1][j]+dp[2][i-1][j]
            print("2번케이스")
            SHOW(dp)

SHOW(dp)
print(sum(dp[i][-1][-1] for i in range(3)))