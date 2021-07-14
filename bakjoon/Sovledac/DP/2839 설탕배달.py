import sys
input=sys.stdin.readline

n=int(input())
# n=18
INF=int(1e9)
d=[INF]*5001
d[0]=0

for i in range(1,n+1):
    if d[i-3]!= INF:
        d[i]=min(d[i],d[i-3]+1)
    if d[i-5]!= INF:
        d[i]=min(d[i],d[i-5]+1)

if d[n]==INF:
    print(-1)
else:
    print(d[n])