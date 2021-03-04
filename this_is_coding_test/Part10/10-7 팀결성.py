def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m= map(int,input().split())
parent=[0] * (n+1)

result=[]

for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    code,a,b=map(int,input().split())
    if code==0:
        union_parent(parent,a,b)
    elif code==1:
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        if a==b:
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)