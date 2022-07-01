from collections import deque

n= int(input())
graph= [[] for _ in range(n+1)]
time={}
answer=[0]*(n+1)
indegree=[0]*(n+1)
for i in range(n):
    arr= list(map(int,input().split()))[:-1]
    a,b= arr[0],arr[1:]
    time[i+1]=a
    for j in range(len(b)):
        indegree[i+1]+=1
        graph[b[j]].append(i+1)

q=deque()
total = 0
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now =q.popleft()
    answer[now]+=time[now]
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            answer[i]= max(answer[i],answer[now])
            q.append(i)

for i in answer:
    print(i)