import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
cmd=[list(map(int,input().split())) for _ in range(m)]

data = [ [0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        data[i][j]=graph[i-1][j-1]
        data[i][j]=data[i][j]+data[i-1][j]+data[i][j-1]-data[i-1][j-1]

answer=[]
for a,b,c,d in cmd:
    answer.append(data[a-1][b-1]-data[c][b-1]-data[a-1][d]+data[c][d])

for i in answer:
    print(i)