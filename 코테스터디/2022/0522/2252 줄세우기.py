from collections import deque

n,m = map(int,input().split())

indegree= [0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b= map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)


q= deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

answer=[]
while q:
    now = q.popleft()
    answer.append(now)
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)


print(*answer)