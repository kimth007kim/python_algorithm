n= int(input())
graph=[[]]
d=[[0]*(n+1) for i in range(n+1)]
for i in range(n):
    graph.append(list(map(int,input().split())))

# print(graph[1][0])
d[1][1]=graph[1][0]
for i in range(2,n+1):
    for j in range(n+1):
        d[i][j]= d[i-]
print(d)