def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    print(a,b)
    if a== b:
        return
    parent[a]=b

answer=1
n,m = map(int,input().split())
parent= [i for i in range(n+1)]
enemy=[0 for _ in range(n+1)]


for _ in range(m):
    a,b= map(int,input().split())
    if find_parent(parent,a)== find_parent(parent,b):
        print(0)
        break
    else:
        aa= enemy[a]
        bb= enemy[b]
        print("aa",aa,"bb",bb)

        if aa !=0:
            union_parent(parent,aa,b)
        else:
            enemy[a]=b
        if bb!=0:
            union_parent(parent,a,bb)
        else:
            enemy[b]=a
else:
    print(1)