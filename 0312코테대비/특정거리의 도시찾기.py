# N:도시갯수, M:도로갯수 ,K: 거리정보 , X출발 도시
from collections import deque



n,m,k,x=map(int,input().split())
graph=[[]for i in range(n+1)]
distance=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(start):
    result=[]
    q=deque()
    q.append(start)
    while q:
        s = q.popleft()
        for i in graph[s]:
            if distance[i] == 0:
                distance[i]+=distance[s]+1
                q.append(i)
    check= False
    for i in range(1,n+1):
        if distance[i]==k:
            print(i)
            check=True
    if check==False:
        print(-1)

# print(bfs(1))
bfs(1)