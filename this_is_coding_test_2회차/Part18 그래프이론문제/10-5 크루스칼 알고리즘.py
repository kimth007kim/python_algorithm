

def find_parent(x,parent):
    if parent[x]!= x:
        parent[x]=find_parent(parent[x],parent)
    return parent[x]

def union_parent(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)

    if a> b:
        parent[a]=b
    else:
        parent[b]=a

n,m= map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
print(parent)
edge=[]
for i in range(m):
    a,b,cost=map(int,input().split())
    edge.append((cost,a,b))

edge.sort()
result=0
for edges in edge:
    cost,a,b=edges
    if find_parent(a,parent) != find_parent(b,parent):
        union_parent(a,b,parent)
        result+=cost

print(result)
