n = int(input())
graph= [[] for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    for i in graph[now]:
        if visited[i]==0:
            visited[i]=now
            print(visited)
            dfs(i)
dfs(1)
print(visited)