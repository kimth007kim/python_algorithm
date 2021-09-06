# https://www.acmicpc.net/problem/16940
import sys

input = sys.stdin.readline

from collections import deque

n= int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer=[0]
tmp = list(map(int,input().split()))
for i in tmp:
    answer.append(i)

visited=[False]*(n+1)
distance=[[i,[]]for i in range(n+1)]

q=deque([(1,0)])
visited[1]=True

while q:
    now,dist= q.popleft()
    for i in graph[now]:
        if not visited[i]:
            distance[now][1].append(i)
            visited[i]=True
            q.append((i,dist+1))
print(distance)
print(answer)

isZero=False

# for i in range(1,n+1):
#     if distance[i]<distance[answer[i - 1]]:
#         isZero=True
#         break
# if isZero:
#     print(0)
# else:
#     print(1)
    # print(distance[i],answer[i],distance[answer[i]])
# print(distance)