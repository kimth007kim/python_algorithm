import sys
sys.setrecursionlimit(100000)

def find_parent(x,parent):
    # print(parent[x],x)
    if parent[x]!=x:
        parent[x]=find_parent(parent[x],parent)
    return parent[x]


def union_parent(a,b,parent):
    A=find_parent(a,parent)
    B=find_parent(b,parent)
    if A>B:
        parent[A]=B
    else:
        parent[B]=A

n,m= map(int,input().split())
parent =[0]*(n+1)
answer=[]
for i in range(len(parent)):
    parent[i]=i
for i in range(m):
    cmd,a,b =map(int,input().split())
    if cmd==0:
        union_parent(a,b,parent)
        # print(parent,a,b)
    else:
        A=find_parent(a,parent)
        B=find_parent(b,parent)
        if A!=B:
            answer.append("NO")
        else:
            answer.append("YES")


for i in answer:
    print(i)