from itertools import combinations
import sys

input =sys.stdin.readline
def dfs(now,next,cnt):
    if visited[now][next]<cnt:
        return
    visited[now][next]=cnt
    for i in graph[next]:
        dfs(now,i,cnt+1)

def score(a,b,MIN):
    total=0
    for i in range(1,n+1):
        total+= min(visited[a][i],visited[b][i])
    total*=2
    if MIN>=total:
        MIN=total
        answer.append([a,b,total])

n,m = map(int,input().split())
graph= [[] for _ in range(n+1)]
answer=[]
INF=int(1e9)
visited=[[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    visited[i][i]=0

for i in range(1,n+1):
    for j in graph[i]:
        dfs(i,j,1)

comb = combinations(range(1,n+1),2)
MIN=int(1e9)
for a,b in list(comb):
    score(a,b,MIN)
answer.sort(key = lambda x:(x[2],x[0],x[1]))
print(answer[0][0],answer[0][1],answer[0][2])