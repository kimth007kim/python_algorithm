from collections import deque

v = int(input())
indegree = [0]*(v+1)
graph= [[] for _ in range(v+1)]

for i in range(v):
    d=list(map(int,input().split()))
    a=d[0]
    del d[0]
    d.pop()
    for j in d:
        print(j)
        graph[i].append(j)
        indegree[j]+=1

print(graph)

def topology_sort():
    q= deque()
    result=[]

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1

            if indegree[i]==0:
                q.append(i)
    print(result)

topology_sort()

# 각 강의의 강의 시간 , 먼저들어야되는 강의 번호 , -1
# 각 강의번호는 1~N


# 입력
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1


# 출력
# 10
# 20
# 14
# 18
# 17
