def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b = find_parent(parent, b)
    if b>a:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

graph=[]
for i in range(e):
    a,b,dist=map(int,input().split())
    graph.append((dist,a,b))

graph.sort()
result=0
for data in graph:
    dist,a,b= data
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=dist

print(result)