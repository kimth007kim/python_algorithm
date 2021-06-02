t= int(input())
result=[]
for _ in range(t):
    cnt = 0
    n= int(input())
    number=list(map(int,input().split()))
    parent=[0]*(n+1)
    for i in range(1,n+1):
        parent[i]=i

    # print(d[3])
    def find_parent(parent,x):
        if parent[x] != x:
            parent[x]= find_parent(parent,parent[x])
        return parent[x]

    def union_parent(a,b):
        a= find_parent(parent,a)
        b= find_parent(parent,b)

        if a>b:
            parent[a]=b
        else:
            parent[b]=a

    for i in range(1,n+1):
        a= parent[i]
        b= number[i-1]
        if find_parent(parent,a)==find_parent(parent,b):
            cnt+=1
        else:
            union_parent(a,b)
    check=[]

    # for i in range(1,n+1):
    #     if parent[i] not in check:
    #         check.append(parent[i])
    #         cnt+=1
    result.append(cnt)

for k in result:
    print(k)