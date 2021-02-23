import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n,m= map(int,input().split())
start= int(input())
distance=[INF]*(n+1)
graph=[[]for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
print(graph)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]<dist:
            continue
        print("now",now)
        for i in graph[now]:
            print("i[0]",i[0])
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]== INF:
        print("INF")
    else:
        print(distance[i])