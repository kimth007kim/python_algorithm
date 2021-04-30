from collections import deque
import copy

n= int(input())
time=[0]*(n+1)
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(1,n+1):
    data=list(map(int,input().split()))
    data.pop()
    time[i]=data.pop(0)
    if len(data)>=1:
        for j in data:
            graph[j].append(i)
            indegree[i]+=1

print(indegree,graph,time)

def topology():
    result=copy.deepcopy(time)
    tot=[]
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        tot.append(now)
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])
topology()
# print(result)