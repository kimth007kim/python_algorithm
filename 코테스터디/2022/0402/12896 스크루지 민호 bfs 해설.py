import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx):
    visited=[-1]*(n+1)
    visited[idx]=0
    q=deque([idx])
    while q:
        now = q.popleft()
        for _next in graph[now]:
            if visited[_next]==-1:
                visited[_next]=visited[now]+1
                q.append(_next)
    node=0
    cnt=0
    for i in range(1,n+1):
        if cnt< visited[i]:
            cnt = visited[i]
            node=i
    return node,cnt

n= int(input())
graph= [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

first,firstdist= bfs(1)
print(first,firstdist)
second,diameter=bfs(first)
print(second,diameter)
print((diameter+1)//2)