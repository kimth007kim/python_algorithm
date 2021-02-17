import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m = map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        print("q에담김",q)
        dist,now=heapq.heappop(q)
        print("dist,now",dist,now)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            print(graph[now])
            cost =dist+i[1]
            print("cost,dist+i[1]",cost,dist,i[1],"distance[i[0]]",distance[i[0]])
            if cost <distance[i[0]]:
                print("cost가 더작음")
                print()
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                print("q=",q)

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])