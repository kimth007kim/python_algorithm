import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())
distance=[INF]*(n+1)


graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))

start,end=map(int,input().split())
q=[]
heapq.heappush(q,(0,start))
distance[start]=0
# now,dist
while q:
    dist,now=heapq.heappop(q)
    # print(dist,now)
    if distance[now]<dist:
        continue
    for i in graph[now]:
        cost=dist+i[1]
        if distance[i[0]]>cost:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))

print(distance[end])