from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

t= int(input())
for _ in range(t):
    n,k=map(int,input().split())
    time=[0]
    temp=list(map(int,input().split()))
    for i in temp:
        time.append(i)
    graph=[[] for i in range(n+1)]
    indegree=[0]*(n+1)

    q= deque()

    for _ in range(k):
        x,y=map(int,input().split())
        graph[x].append(y)
        indegree[y]+=1

    win = int(input())

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    print("time =",time)

    result = deepcopy(time)

    while q:
        now= q.popleft()
        print("now",now)
        if now == win:
            break

        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
        print(result)

    print(result[win])