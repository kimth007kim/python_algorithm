from collections import deque

n,m,k= map(int,input().split())
time =list(map(int,input().split()))
def topology_sort(indegree,time):
    result =time[0]
    q = deque()
    q.append(1)
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                result+=time[i-1]
                q.append(i)
    print(result)

graph=[[] for _ in range(n+1)]
indegree=[0 for _ in range(n+1)]
print(time,indegree)

for i in range(m):
    a,b = map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)

for i in range(n):
    t= time[:]
    t[i]=0
    topology_sort(indegree[:],t)



# topology_sort()
print(indegree, graph)
