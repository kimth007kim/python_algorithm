def find_parent(x,parent):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x],parent)
    return parent[x]

def union_parent(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a


n,m=map(int,input().split())
parent=[i for i in range(n)]

edges=[]
for i in range(m):
    x,y,cost=map(int,input().split())
    edges.append((cost,x,y))

edges.sort()
print(edges)

result=0
total=0
for edge in edges:
    cost, x, y = edge
    total+=cost
    if find_parent(x,parent) != find_parent(y,parent):
        union_parent(x,y,parent)
        result+=cost

print(total-result)
