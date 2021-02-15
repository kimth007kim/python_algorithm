import heapq
import sys
input =sys.stdin.readline()
INF=int(1e9)                    # 무한을 의미하는 값 10억

n,m=map(int,input().split())    # 노드의 개수,간선의 개수를 입력받기
start=int(input())              # 시작 노드 번호를 입력받기
graph=[[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
distance=[INF]*(n+1)            # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):              # 모든 간선 정보를 입력받기
    a,b,c=map(int,input().split())# a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstar(start):
    q=[]
    heapq.heappush(q(0,start))   #시작 노드로 가기위한 최단경로는 0으로 설정하여 큐에 삽입
    distance[start]=0
    while q:                    #큐가 비어있지 않다면
        dist,now=heapq.heappop(q)  #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now]<dist:  #현재 노드가 이미 처리된적이 있는 노드라면 무시
            continue
        for i in graph[now]:    #현재 노드와 연결된 다른 인접한 노드를 확인
            cost =dist +i[1]
            if cost<distance[i[0]]:# 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstar(start)     # 다익스트라 알고리즘을 수행

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])