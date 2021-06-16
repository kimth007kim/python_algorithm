import heapq

INF=int(1e9)

n,m=map(int,input().split())
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q=[]
heapq.heappush(q,(0,1))
distance[1]=0
while q:
    dist,now=heapq.heappop(q)
    if dist>distance[now]:
        continue
    for i in graph[now]:
        cost=dist+i[1]
        print(distance[i[1]],cost)
        if distance[i[0]]>cost:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))

Vmax=0
cnt=0
for i in range(1,n+1):
    if distance[i]>Vmax:
        Vmax=distance[i]
        index=i
        cnt=0
    if distance[i]==Vmax:
        cnt+=1

print(distance)
print(index,Vmax,cnt)
