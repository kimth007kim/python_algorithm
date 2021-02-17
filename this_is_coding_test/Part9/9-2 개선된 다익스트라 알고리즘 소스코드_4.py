import sys
import heapq
INF=int(1e9)
input= sys.stdin.readline

n,m= map(int,input().split())
start=int(input())
graph=[[]for _ in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in distance:
    if i==INF:
        print("무한대")
    else:
        print(i)