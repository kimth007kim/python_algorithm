import sys

input = sys.stdin.readline


n= int(input())

data = []
d=[0]*(n+1)
for i in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

for i in range(n-1,-1,-1):
    if data[i][0] +i<=n:
        value,distance= data[i][0],data[i][1]
        MAX=0
        for j in range(i+value,n):
            MAX=max(MAX,d[j])
        d[i]=max(d[i],MAX+distance)

d.sort(reverse=True)
print(d[0])