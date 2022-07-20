import sys

input =sys.stdin.readline

n,m = map(int,input().split())

graph= []
for i in range(n):
    graph.append(list(map(int,input().split())))
prefix = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    prev=0
    for j in range(1,m+1):
        prev+=graph[i-1][j-1]
        prefix[i][j]=prev

for i in range(1,m+1):
    prev=0
    for j in range(1,n+1):
        prev+=prefix[j][i]
        prefix[j][i]=prev
dp = [[0]*(m+1) for _ in range(n+1)]
MAX=-int(1e11)
for i in range(1,n+1):
    for j in range(1,m+1):
        for x in range(i):
            for y in range(j):
                MAX=max(MAX,prefix[i][j]-(prefix[i][y]+prefix[x][j])+prefix[x][y])

print(MAX)