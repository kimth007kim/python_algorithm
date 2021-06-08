n,m=map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(a,b,parent):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a
for _ in range(m):
    a,b=map(int,input().split())
    if find_parent(parent,a)!= find_parent(parent,b):
        union_parent(a,b,parent)

result=[]
for i in parent:
    result.append(find_parent(parent,i))
result = result[1:]
print(len(set(result)))