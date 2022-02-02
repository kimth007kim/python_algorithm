# n= 출발지
# k= 목적지
from collections import deque
import sys

input = sys.stdin.readline

q = deque()
n,k = map(int,input().split())
INF= int(1e9)
dp=[INF]*100001
# dp=[INF]*101
LEN= len(dp)
q.append([5,0])
dp[n]=0
while q:
    number,cnt=q.popleft()
    # print(q)
    if number>LEN or number<0:
        continue
    # if
    if 0<number * 2 < len(dp):
        if dp[number * 2] > cnt:
            q.appendleft([number * 2, cnt])
            dp[number * 2] = cnt
    if number+1<=LEN-1:
        if dp[number+1]>cnt+1:

            q.append([number+1,cnt+1])
            dp[number+1]=cnt+1
        if dp[number-1]>cnt+1:
            q.append([number-1,cnt+1])
            dp[number -1] = cnt + 1

# for i in range(LEN):
#     print(i,dp[i])
print(dp[k])
# for i in range()