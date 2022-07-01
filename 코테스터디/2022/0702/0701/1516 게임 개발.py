from collections import deque
import sys

input=sys.stdin.readline

n = int(input())
distance={}
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
answer= [0]*(n+1)
for i in range(1,n+1):
    tmp = list(map(int,input().split()))[:-1]
    distance[i]=tmp[0]
    for j in tmp[1:]:
        graph[j].append(i)
        indegree[i]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)


while q:
    now = q.popleft()
    answer[now]+=distance[now]
    for i in graph[now]:
        indegree[i]-=1
        answer[i]= max(answer[i],answer[now])
        if indegree[i]==0:
            q.append(i)



for i in range(1,n+1):
    print(answer[i])