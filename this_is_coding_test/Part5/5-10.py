# 연결요소찾기
# DFS 혹은 BFS로 해결가능하다.

n,m= map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
# print(graph)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        print(graph)
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        print(x,y)
        dfs(x-1,y)
        print("x-1,y",x-1,y,dfs(x-1,y))
        dfs(x,y-1)
        print("x,y-1",x,y-1,dfs(x,y-1))
        dfs(x+1,y)
        print("x+1,y",x+1,y,dfs(x+1,y))
        dfs(x,y+1)
        print("x,y+1",x,y+1,dfs(x,y+1))
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        # print(i,j)
        if dfs(i,j)== True:
            result +=1
            print(result)

print(result)

# for i in range(4):
#     for j in range(5):
#         print(graph[i][j])
#     print(i,"끝")