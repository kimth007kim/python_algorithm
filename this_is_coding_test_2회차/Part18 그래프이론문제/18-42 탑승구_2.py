
def find_parent(parent,x):
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(a,b,parent):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

n= int(input())
m= int(input())

parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

result=0
for i in range(1,m+1):
    data= find_parent(parent,int(input()))
    if data==0:
        break
    union_parent(data,data-1,parent)
    result+=1
    print(parent)

print(result)