import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(now,prev):
    global ans
    dist= 0
    for v in graph[now]:
        if v!=prev:
            # dist=dfs(next,now)
            dist= max(dist,dfs(v,now))

    if dist>=d:
        ans+=1
    return dist+1

n,s,d = map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans=0
dfs(s,0)


print((ans-1)*2 if ans else 0)