# n= 출발지
# k= 목적지
from collections import deque
import sys
from collections import deque
input = sys.stdin.readline

n,k= map(int,input().split())


q= deque()
visited=[-1 for _ in range(100001)]
visited[n]=0
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        print(visited[k])
        break

    if 0<=now-1<100001 and visited[now-1]==-1:
        visited[now-1] = visited[now]+1
        q.append(now-1)
    if 0<=now+1<100001 and visited[now+1]==-1:
        visited[now+1] = visited[now]+1
        q.append(now+1)
    if 0<=now*2<100001 and visited[2*now]==-1:
        visited[2*now]=visited[now]
        q.appendleft(now*2)



