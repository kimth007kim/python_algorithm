import sys

input = sys.stdin.readline

n= int(input())
graph= [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = list(map(int,input().split()))

level = [False]*(n+1)
tsize=[0]*(n+1)
visited=[False]*(n+1)

print("level",level)
print("tsize",tsize)
print("visited",visited)

def dfs(x,lv):
    if visited[x]:
        return 0
    visited[x]=True
    size=1
    level[x]=lv
    for i in range(len(graph[x])):
        next= graph[x][i]
        size+=dfs(next,lv+1)
    tsize[x]=size
    print(tsize)
    return size

if answer[0]!=1:
    print("0")
else:
    dfs(1,0)
    print("tsize 두번째",tsize)
    print("answer",answer)
    for i in range(1,n):
        x= answer[i]
        print(x)
        if tsize[x]==1 or i+tsize[x]>=n:
            continue
        next = answer[i+tsize[x]]
        print(next)
        if level[next]>level[x]:
            print(0)
            break
        print(i)