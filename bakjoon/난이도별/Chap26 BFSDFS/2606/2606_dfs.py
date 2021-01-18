
cnt= int(input())
num =int(input())

answer=[]


graph=[[] for _ in range(cnt+1)]
visited=[False] * (cnt+1)
for i in range(num):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in graph:
    j.sort()


def dfs(v):
    visited[v]=True
    # print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            answer.append(i)

dfs(1)
print(len(answer))