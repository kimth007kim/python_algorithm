import heapq

INF=int(1e9)
n,m=map(int,input().split())

graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

print(graph)


def dijikstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist> distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijikstra(1)
low=-1
for i in range(1,n+1):
    if distance[i]>low:
        low=distance[i]
        cnt=0
        index=i
    if distance[i]==low:
        cnt+=1
print(index,distance[index],cnt)
