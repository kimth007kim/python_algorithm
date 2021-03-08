from collections import deque

v,e = map(int,input().split())
indegree= [0]* (v+1)
graph=[[]for i in range(v+1)]

for i in range(e):
    a,b =map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    q=deque()
    result=[]

    for i in range(v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

topology_sort()

