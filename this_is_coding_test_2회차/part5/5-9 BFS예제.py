from collections import deque
def bfs(graph,start,visited):
    q=deque()
    q.append(start)
    # q = deque([start])
    visited[start]=True
    while q:
        v= q.popleft()
        print(v,end=" ")
        for i in graph[v]:
            # print("i",i)
            if visited[i]==False:
                visited[i]=True
                q.append(i)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9


bfs(graph,1,visited)