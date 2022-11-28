from heapq import heappush,heappop
import sys

input =sys.stdin.readline

INF = int(1e11)
v,e,p = map(int,input().split())

graph=[[] for _ in range(v+1)]
visited=[INF]*(v+1)

for i in range(e):
    a,b,c= map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

q= []
if p==1:
    heappush(q,[0,1,True])
else:
    heappush(q,[0,1,False])

visited[1]=0
answer_flag,answer_dist=False,INF
while q:
    # print(q)
    dist,now,flag=heappop(q)

    if now ==v:
        if answer_dist>=dist:
            if answer_flag==True:
                answer_flag,answer_dist=True,dist
            else:
                answer_flag,answer_dist=flag,dist

    for i in graph[now]:
        cost= dist+i[1]
        if visited[i[0]]>=cost:
            visited[i[0]]=cost
            if i[0]==p:
                heappush(q,[cost,i[0],True])
            else:
                heappush(q,[cost,i[0],flag])

if answer_flag==True:
    print("SAVE HIM")
else:
    print("GOOD BYE")

