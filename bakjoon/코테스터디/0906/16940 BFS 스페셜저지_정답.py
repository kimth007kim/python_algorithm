from collections import deque


n=int(input())
graph= [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()

answer= list(map(int,input().split()))
stk=[]
flag=False
visited=[False]*(n+1)

def bfs(n):
    global flag
    q=deque()
    visited[n]=True
    q.append(n)
    start=1
    tmp=[]
    while q:
        print(q)
        stk=[]
        for i in graph[q.popleft()]:
            if not visited[i]:
                visited[i]=True
                stk.append(i)
        li = answer[start:start+len(stk)]
        li.sort()
        if li!=stk:
            flag=True
            break
        else:
            for i in tmp:
                q.append(i)



if answer[0]==1:
    bfs(1)
    print(1) if not flag else print(0)
else:
    print(0)
