import sys

input= sys.stdin.readline


n,m = map(int,input().split())
k=int(input())
graph=[list(input().rstrip()) for _ in range(n)]
cmd=[]



jungle=[[0]*(m+1) for _ in range(n+1)]
ocean=[[0]*(m+1) for _ in range(n+1)]
ice=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i-1][j-1]=="J":
            jungle[i][j]+=1
        if graph[i-1][j-1]=="O":
            ocean[i][j]+=1
        if graph[i-1][j-1]=="I":
            ice[i][j]+=1
        jungle[i][j]=jungle[i-1][j]+jungle[i][j-1]-jungle[i-1][j-1]+jungle[i][j]
        ocean[i][j]=ocean[i-1][j]+ocean[i][j-1]-ocean[i-1][j-1]+ocean[i][j]
        ice[i][j]=ice[i-1][j]+ice[i][j-1]-ice[i-1][j-1]+ice[i][j]

for k in range(k):
    a,b,c,d= map(int,input().split())
    cmd.append([a,b,c,d])
    print(jungle[c][d]-jungle[c][b-1]-jungle[a-1][d]+jungle[a-1][b-1],end=" ")
    print(ocean[c][d]-ocean[c][b-1]-ocean[a-1][d]+ocean[a-1][b-1],end=" ")
    print(ice[c][d]-ice[c][b-1]-ice[a-1][d]+ice[a-1][b-1])

