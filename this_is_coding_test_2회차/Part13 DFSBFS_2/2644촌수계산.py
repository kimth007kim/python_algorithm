from collections import deque

n=int(input())
start,end=map(int,input().split())
m=int(input())
visit=[-1]*(n+1)
data=[[] for _ in range(n+1)]
for i in range(m):
    t1,t2= map(int,input().split())
    data[t1].append(t2)
    data[t2].append(t1)
q=deque()
q.append(start)
visit[start]=0
while q:
    now = q.popleft()
    # print(now)
    for i in data[now]:
        if visit[i]==-1:
            visit[i]= visit[now]+1
            q.append(i)

print(visit[end])