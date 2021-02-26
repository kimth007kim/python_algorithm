import sys
import heapq
INF=int(1e9)
input=sys.stdin.readline

n,e = map(int,input().split())
graph=[[] for i in range(n+1)]


for _ in range(e):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start):
    q=[]
    distance = [INF] * (n + 1)
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

result1=dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[n]
result2=dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[n]
result=min(result1,result2)

if result>=INF:
    print(-1)
else:
    print(result)