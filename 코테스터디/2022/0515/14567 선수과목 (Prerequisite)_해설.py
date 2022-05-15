from collections import deque


n,m = map(int,input().split())
result={}
for i in range(1,n+1):
    result[i]=0
indegree= [0]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append([i,1])
while q:
    print(q)
    now,cnt = q.popleft()
    result[now]=cnt
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append([i,cnt+1])
print(result)