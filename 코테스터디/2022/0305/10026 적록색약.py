from collections import deque

n = int(input())
graph=[]
visited=[[False]*n for _ in range(n)]
new_graph=[[False]*n for _ in range(n)]
new_visited=[]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(graph,visit,x,y):
    q=deque()

for _ in range(n):
    arr=list(input())
    tmp=[]
    for i in arr:
        if i =="R" or i =="G":
            tmp.append("R")
        else:
            tmp.append("B")
    graph.append(arr)
    new_graph.append(tmp)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph,visited,i,j)
            if not visited[i][j]:
                bfs(graph, visited, i, j)
            print(i,j,graph[i][j])

