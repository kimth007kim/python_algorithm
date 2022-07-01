from collections import deque

n= int(input())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
result=[0]*(n+1)
distance={}
for i in range(1,n+1):
    tmp = list(map(int,input().split()))[:-1]
    num,arr= tmp[0],tmp[1:]
    distance[i]=num
    for j in arr:
        graph[j].append(i)
        indegree[i]+=1



q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
while q:
    now =q.popleft()
    result[now]+= distance[now]
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            result[i]= max(result[i],result[now])
            q.append(i)
result = result[1:]
for i in result:
    print(i)