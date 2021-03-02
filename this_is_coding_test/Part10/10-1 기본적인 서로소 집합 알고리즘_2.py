def find_parent(parent,x):
    print("parent[x],x",parent[x],x)
    if parent[x]!= x:
        print("부모아님")
        return find_parent(parent,parent[x])
    return x
def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b
v,e = map (int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)
    print(parent)