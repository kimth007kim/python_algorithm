def check_parent(parent,x):
    if parent[x]!=x:
        check_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=check_parent(parent,a)
    b=check_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())

parent= [0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

for i in range(1,v+1):
    print(parent[i],end=' ')