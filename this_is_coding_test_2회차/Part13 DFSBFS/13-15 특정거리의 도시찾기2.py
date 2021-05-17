import heapq

INF=int(1e9)
n,m,k,x=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

print(graph)

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]< dist:
            continue
        for i in graph[now]:
            cost= dist+i[1]
            if cost< distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(x)

print(distance)