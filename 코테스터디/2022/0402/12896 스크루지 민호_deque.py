from collections import deque
import sys

input = sys.stdin.readline
# n개의 도시
# 양방향 도로
n= int(input())
road= []
INF=int(1e9)
visited=[[INF]*(n) for _ in range(n)]
graph=[[] for _ in range(n+1)]
q=deque()
for i in range(n):
    for j in range(n):
        if i==j:
            visited[i][j]=0
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    q.append([1,a,b])
    q.append([1,b,a])
while q:
    cnt,x,y= q.popleft()
    if visited[x-1][y-1]>cnt:
        visited[x-1][y-1]=cnt
        for i in graph[y]:
            if visited[x-1][i-1]>cnt:
                q.append([cnt+1,x,i])

MAX=int(1e9)
SUM=int(1e9)
for i in range(n):
    tmp_sum=0
    tmp_mx=-1
    for j in range(n):
        tmp_sum+=visited[i][j]
        tmp_mx=max(visited[i][j],tmp_mx)
    if SUM>tmp_sum:
        SUM=tmp_sum
        MAX=tmp_mx
print(MAX)