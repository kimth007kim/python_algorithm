# 1  // T=test케이스 개수
# 4 4 //N,K N=건물개수 K=건설순서 규칙
# 10 1 100 10 건물당 건설에걸리는 시간
# 1 2 건설순서 x,y x->y지어야됨
# 1 3 건설순서 x,y x->y지어야됨
# 2 4 건설순서 x,y x->y지어야됨
# 3 4 건설순서 x,y x->y지어야됨
# 4  //승리하기위해 건설해야하는 건물

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

t= int(input())
n,k=map(int,input().split())
d=list(map(int,input().split()))

parent=[0]*(n+1)
edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

for _ in range(k):
    a,b=map(int,input().split())
    cost=d[a-1]
    edges.append((cost,a,b))
w= int(input())

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!= find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)







