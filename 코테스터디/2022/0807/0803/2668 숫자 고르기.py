import sys

input=sys.stdin.readline


n= int(input())
graph=[[] for _ in range(n+1)]
answer=[]
def dfs(now,origin):
    visited[now]=True

    if visited[origin]==True and now == origin:
        answer.append(origin)
        return
    for i in graph[now]:
        if visited[i]==False:
            dfs(i,origin)

for i in range(1,n+1):
    t= int(input())
    graph[i].append(t)

for i in range(1,n+1):
    visited=[False]*(n+1)
    for j in graph[i]:
        dfs(j,i)
print(len(answer))
for i in answer:
    print(i)