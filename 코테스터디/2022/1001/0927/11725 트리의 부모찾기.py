from collections import defaultdict,deque

n= int(input())
graph = defaultdict(list)
q=deque()
parent=[-1]*(n+1)
visited=[False]*(n+1)
for i in range(n-1):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q.append([1,1])
parent[1]=1
while q:
    now,prev=q.popleft()
    for i in graph[now]:
        if parent[i]==-1:
            parent[i]=now
            q.append([i,now])

answer= parent[2:]
for i in answer:
    print(i)