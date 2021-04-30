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

n,m = map(int,input().split())

parent=[0]*(n+1)
result=0
edges=[]
for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()


for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        print(cost,a,b,"parent[a]",parent[a],"parent[b]",parent[b] )
        result+=cost
        union_parent(parent,a,b)
        last=cost

print(result-last)
