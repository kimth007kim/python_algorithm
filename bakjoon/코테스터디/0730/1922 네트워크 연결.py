def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a


n=int(input())  #컴퓨터의 수
m=int(input())  #간선의 수
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
edge=[]
result=0
for i in range(m):
    a,b,cost=map(int,input().split())
    edge.append((cost,a,b))

edge.sort()
for e in edge:
    cost,a,b=e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)