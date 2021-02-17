import sys
input=sys.stdin.readline
INF = int(1e9)

n,m= map(int,input().split())       # 노드,간선의 개수 입력받기
start=int(input())                  # 시작 노드 번호를 입력받기
graph=[[] for i in range(n+1)]      # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
visited=[False]*(n+1)               # 방문한 적이 있는 노드에 대한 정보를 담는 리스트를 만들기
distance=[INF]*(n+1)                # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):                  #모든 간선의 정보를 입력받기
    a,b,c=map(int,input().split())
    graph[a].append((b,c))          #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    
def get_smallest_node():            #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value=INF
    index=0                         #가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):                # 시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    for i in range(n-1):            # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        now=get_smallest_node()     # 현재 최단 거리가 가장 짧은 노드를 꺼내서,방문처리
        visited[now]=True
        for j in graph[now]:        # 현재 노드와 연결된 다른 노드를 확인
            cost=distance[now]+j[i]
            if cost <distance[j[0]]:# 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]]=cost
    
dijkstra(start)                     # 다익스트라 알고리즘 수행

for i in range(1,n+1):              #모든 노드로 가기위한 최단거리를 출력
    if distance[i]==INF:            #도달할 수 없는 경우, 무한 (INFINITY)이라고 출력
        print("INFINITY")
    else:                           #도달할 수있는 경우 거리를 출력
        print(distance[i])