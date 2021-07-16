import sys

input=sys.stdin.readline
n,k=map(int,input().split())

d=[[1]*i for i in range(1,32)]



for i in range(2,30):
    # print(d[i])
    for j in range(len(d[i])):
        if j==(len(d[i])-1) or j==0:
            d[i][j]=1
        else:
            d[i][j]=d[i-1][j-1]+d[i-1][j]

print(d[n-1][k-1])