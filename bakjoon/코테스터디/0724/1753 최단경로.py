import sys
import heapq
input=sys.stdin.readline

v,e= map(int,input().split())
k=int(input())
graph=[[] for _ in range(v+1)]

INF=int(1e9)

distance=[INF]*(v+1)
for i in range(e):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))

q=[]
heapq.heappush(q,(0,k))
distance[k]=0

while q:
    dist,now=heapq.heappop(q)
    for i in graph[now]:
        cost=dist+i[1]
        if distance[i[0]]>cost:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))


for i in range(1,len(distance)):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])