from collections import deque
import sys

input = sys.stdin.readline
q=deque()

n,s,d = map(int,input().split())
graph= [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def dfs(now,depth):
    global total
    total+=1
    print(now,depth,visited,total)
    if len(graph[now])==1 and now != s:
        # print("빼기전",total)
        total-=d
        # print("뺀후",total)
        # if depth-d>0:
        #     total+=depth-d
        return
    visited[now]=True
    for i in graph[now]:
        if visited[i]==False:
            dfs(i,depth+1)

total=0
dfs(s,0)
print((total-1)*2)