import sys
input = sys.stdin.readline

n= int(input())
# 집은 빨강 초록 파랑 중 하나의 색으로 칠해야한다. 각각의 집을 빨강 초록 파랑으로 칠하는 비용이 주어졌을때,
# 모든 집을 칠하는 비용은?

color=[]
for i in range(n):
    r,g,b=map(int,input().split())
    color.append((r,g,b))


graph=[[0]*n for _ in range(n)]
for i in range(3):
    graph[0][i]= color[0][i]

for i in range(1,n):
    for j in range(3):
        if j==0:
            a=1
            b=2
        elif j==1:
            a=0
            b=2
        else:
            a=0
            b=1
        graph[i][j]=color[i][j]+min(graph[i-1][a],graph[i-1][b])

MINVALUE=int(1e9)
for i in range(3):
    MINVALUE=min(MINVALUE,graph[n-1][i])

print(MINVALUE)