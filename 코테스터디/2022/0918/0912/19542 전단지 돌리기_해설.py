
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dfs(cur,past):
    global ans


    dist = 0
    for v in graph[cur]:
        if v!=past:
            dist =max(dist,dfs(v,cur))

    if dist>=d:
        ans+=1
    return dist+1

n,s,d= map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
ans=0
dfs(s,0)

print(ans)