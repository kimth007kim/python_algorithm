from heapq import heappop,heappush
import sys


def dajikstra(start):

    distance=[INF]*(n+1)
    q=[]
    distance[start]=0
    heappush(q,[0,start])
    while q:
        d,now=heappop(q)
        for next,nd in graph[now]:
            cost=d+nd
            if cost<distance[next]:
                distance[next]=cost
                heappush(q,[cost,next])
        # print(d,now)
    for i in range(1,n+1):
        total[i]=min(total[i],distance[i])
    # print(distance)

input = sys.stdin.readline
INF=int(1e11)
n= int(input())
a,b,c= map(int,input().split())


graph=[[] for _ in range(n+1)]
total=[INF]*(n+1)
for i in range(int(input())):
    x,y,z=map(int,input().split())
    graph[x].append([y,z])
    graph[y].append([x,z])

dajikstra(a)
dajikstra(b)
dajikstra(c)
# print(total)
MAX=0
answer=1
# print(total)
for i in range(1,n+1):
    if total[i]>MAX:
        MAX=total[i]
        answer=i

print(answer)