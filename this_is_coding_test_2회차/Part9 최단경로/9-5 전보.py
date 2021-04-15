# c라는 도시에 위급상황 발생
# 최대한 많은 도시로 메시지를 보내고자한다.
# 각 도시의 번호와 통로가 설치되어있는 정보가 주어졌을때 c에서 보낸 메시지를 받게되는 도시의개수 는 총 몇개? 받는시간은 얼마?


# n=도시의 개수
# m=통로의 개수
# c=메시지 보내고자 하는도시
import heapq
INF=int(1e9)

n,m,c=map(int,input().split())
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count=0
max_distance=0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)

print(count-1,max_distance)