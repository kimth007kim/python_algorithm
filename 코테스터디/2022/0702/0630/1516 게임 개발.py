from collections import deque
n= int(input())

indegree=[0]*(n+1)
answer=[0]*(n+1)
graph=[[] for _ in range(n+1)]
distance = [0]*(n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))[:-1]
    d,arr= tmp[0],tmp[1:]
    for j in arr:
        indegree[i]+=1
        graph[j].append(i)
    distance[i]=d

q=deque()

for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
print(answer)
while q:
    # print("시작",answer)
    now = q.popleft()
    answer[now]+=distance[now]
    for i in graph[now]:
        indegree[i]-=1
        answer[i]=max(answer[i],answer[now])
        print(answer)
        if indegree[i]==0:
            q.append(i)


for i in range(1,n+1):
    print(answer[i])