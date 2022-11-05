from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph=[set() for _ in range(n+1)]
for i in range(m):
    tmp = list(map(int, input().split()))
    arr= tmp[1:-1]
    s,e = tmp[0],tmp[-1]
    indegree[e]=s


    for j in arr:
        graph[j].add(e)

l= int(input())
potion=list(map(int,input().split()))
answer=set()
q=deque()
# for i in range(1,n+1):
#     if indegree[i]==0:
#         q.append(i)
#         answer.append(i)

for i in potion:
    indegree[i]=0
    q.append(i)
    answer.add(i)
while q:
    now= q.popleft()
    for i in graph[now]:
        if indegree[i]==1:
            indegree[i]=0

            q.append(i)
            answer.add(i)

        elif indegree[i]>1:
            indegree[i]-=1

answer=list(answer)
answer.sort()
print(len(answer))
print(*answer)