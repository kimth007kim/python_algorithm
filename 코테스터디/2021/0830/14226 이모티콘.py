from collections import deque
n=int(input())
d=[[-1]*(n+1) for i in range(n+1)]
visited=[]
def bfs():
    q=deque()
    q.append([1,0])
    d[1][0]=0
    while q:
        x,y= q.popleft()
        if d[x][x]==-1:
            d[x][x]=d[x][y]+1
            q.append([x,x])
        if x+y<=n and d[x+y][y]==-1:
            d[x+y][y]=d[x][y]+1
            q.append([x+y,y])
        if x-1>=0 and d[x-1][y]==-1:
            d[x-1][y]=d[x][y]+1
            q.append([x-1,y])

bfs()
r=d[n][1]
for i in range(1,n):
    if d[n][i]!=-1:
        r=min(r,d[n][i])
        print(r)
print(d)