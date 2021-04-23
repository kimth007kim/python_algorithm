def find_parent(parent,x):
    if parent[x]!= x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b = find_parent(parent, b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

v,e=map(int,input().split())
parent=[0]*(v+1)
cycle=False

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)== find_parent(parent,b):
        cycle=True
    else:
        union_parent(parent,a,b)

if cycle:
    print("발생o")
else:
    print("발생x")