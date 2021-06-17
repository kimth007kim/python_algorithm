import heapq
import sys

input = sys.stdin.readline
INF=int(1e9)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
answer=[]

def hq(n):
    graph = []
    distance = [[INF] * (n) for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    q=[]
    heapq.heappush(q,(graph[0][0],0,0))
    while q:
        dist,x,y=heapq.heappop(q)
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if distance[nx][ny] > dist + graph[nx][ny]:
                    distance[nx][ny]=dist+graph[nx][ny]
                    heapq.heappush(q,(distance[nx][ny],nx,ny))
    answer.append(distance[n-1][n-1])
while True :
    n= int(input())
    if n==0:
        for i in range(len(answer)):
             print("Problem "+str(i+1)+": "+str(answer[i]))
        break
    else:
        hq(n)