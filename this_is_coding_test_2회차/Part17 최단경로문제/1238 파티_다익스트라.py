import heapq
import sys


input = sys.stdin.readline

n,m,x= map(int,input().split())
INF= int(1e9)
graph= [[] for _ in range(n+1)]
ngraph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c= map(int,input().split())
    ngraph[a].append((b,c))

answer=[]
answer.append([])

for cnt in range(1,n+1):
    graph = [[] for _ in range(n + 1)]
    for i in range(1,n+1):
        for a,b in ngraph[i]:
            graph[i].append((a,b))
    distance = [INF] * (n + 1)
    #
    start=cnt
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost =dist+i[1]
            if cost <distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    answer.append(distance)

result=0
for i in range(1,n+1):
    result=max(result,answer[i][x]+answer[x][i])

print(result)