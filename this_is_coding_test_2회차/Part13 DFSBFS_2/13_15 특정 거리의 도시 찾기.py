from collections import deque


n,m,k,x=map(int,input().split())
data=[]
distance=[-1]*(n+1)

data=[[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    data[a].append(b)

print(data)
q=deque([x])
distance[x]=0
while q:
    now = q.popleft()
    for i in data[now]:
        if distance[i] ==-1:
            distance[i]= 1+distance[now]
            q.append(i)

print(distance)