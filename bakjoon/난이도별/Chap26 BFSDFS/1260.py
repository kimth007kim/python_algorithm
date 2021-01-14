from collections import deque

N,M,V= map(int,input().split())

graph=[[] for _ in range(N+1)]
for i in range(M):
    D,S= map(int,input().split())

    graph[D].append(S)
    graph[S].append(D)
print(graph)

# for j in range(N+1):
#     graph[j]=list(set(graph[j]))
#     if j in graph[j]:
#         graph[j].remove(j)

def dfs(graph, v, visited1):
    visited1[v]= True
    print(v,end=" ")

    for i in graph[v]:
        if not visited1[i]:
            dfs(graph,i,visited1)

def bfs(graph,start,visited2):
    queue = deque([start])
    visited2[start]=True


    while queue:
        v= queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

visited1=[False]* (N+1)
visited2=[False]* (N+1)

dfs(graph,V,visited1)
print()
bfs(graph,V,visited2)