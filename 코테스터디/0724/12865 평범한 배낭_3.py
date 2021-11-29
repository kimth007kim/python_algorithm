import sys
input = sys.stdin.readline

n,k= map(int,input().split())
d=[[0]*(k+1) for _ in range(n+1)]



for i in range(1,n+1):
    item,value= map(int,input().split())
    for j in range(k+1):
        if item>j:
            d[i][j] = d[i-1][j]
        else:
            d[i][j]=d[i-1][j-item]+value
            # d[i][j] = max(d[i-1][j],d[i-1][j-item]+value)


for i in d:
    print(i)