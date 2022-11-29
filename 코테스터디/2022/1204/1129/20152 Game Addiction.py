import sys
input =sys.stdin.readline

n,m=map(int,input().split())
wok= list(map(int,input().split()))
wok.sort(reverse=True)
wok_set=set(wok)
for i in range(m):
    for j in range(i+1,m):
        wok_set.add(wok[i]+wok[j])
INF =int(1e11)
dp=[ INF]*(n+1)
dp[0]=0
# for i in wok_set:
#     print(i)
#     if i<=n:
#         dp[i]=1

for i in range(n+1):
    for j in wok_set:
        if i+j<=n:
            dp[i+j]=min(dp[i]+1,dp[i+j])
if dp[-1]==INF:
    print(-1)
else:
    print(dp[-1])