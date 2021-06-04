from collections import deque

n,k= map(int,input().split())

MAX=200000
visited=[False]*(MAX+1)
q=deque()
q.append((n,0))
result=0
while q:
    n,cnt= q.popleft()
    visited[n]=True
    if n==k:
        result=cnt
        break
    for i in ((n+1),(n-1),(n*2)):
        if -1<i <MAX and not visited[i]:
            q.append((i,cnt+1))
    # q.append((n+1,cnt+1))
    # q.append((n-1,cnt+1))
    # q.append((n*2,cnt+1))

print(cnt)