from collections import defaultdict


def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    A= find_parent(parent,a)
    B= find_parent(parent,b)
    if A!=B:
        parent[B]=A
        score[A]+=score[B]
    print(score[A])


for _i in range(int(input())):
    f= int(input())
    parent,score=defaultdict(str),defaultdict(int)
    for _ in range(f):
        p1,p2 = input().split()
        if p1 not in parent:
            parent[p1]=p1
            score[p1]=1
        if p2 not in parent:
            parent[p2]=p2
            score[p2]=1
        union_parent(parent, p1, p2)

