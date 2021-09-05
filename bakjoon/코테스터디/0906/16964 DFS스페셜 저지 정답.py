# https://vixxcode.tistory.com/29


import sys
input=sys.stdin.readline
n= int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = list(map(int,input().split()))

level= [False]*(n+1)
tsize=[0]*(n+1)
visited=[False]*(n+1)


def dfs(x,lv):
    if visited[x]:
        return 0
    visited[x]=True
    size=1
    level[x]=lv
    for i in range(len(graph[x])):
        next=graph[x][i]
        print(next)
        size+=dfs(next,lv+1)
    tsize[x]=size
    return size

if answer[0]!=1:
    print("0")
    sys.exit(0)
else:
    dfs(1,0)
    print(tsize)
    for i in range(1,n):
        x=answer[i]
        if tsize[x]== 1 or i+tsize[x]>=n:
            continue
        next =answer[i+tsize[x]]
        if level[next] > level[x]:
            print(0)
            sys.exit(0)
        print(1)
