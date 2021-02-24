import heapq
import sys
INF=int(1e9)
input=sys.stdin.readline
# n 도시의 개수
# m 통로(간선)의 개수
# c 메세지를 보내고자하는 도시

n,m,c=map(int,input().split())
graph=[[]for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    # x 시작
    # y 도착
    # z 거리
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=i[1]+dist
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

for i in range(0,n+1):
    if distance[i] == int(1e9):
        distance[i] = -1

length= max(distance)
cnt=0
for i in range(2,n+1):
    if distance[i]>0:
        cnt+=1

print(cnt,length)