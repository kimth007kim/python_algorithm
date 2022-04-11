def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    A=find_parent(parent,a)
    B=find_parent(parent,b)
    if A!=B:
        parent[B]=A
        number[A]+=number[B]
    print(number[A])
for _ in range(int(input())):
    num= int(input())
    parent,number={},{}
    for i in range(num):
        a,b=input().split()
        if a not in parent:
            parent[a]=a
            number[a]=1
        if b not in parent:
            parent[b]=b
            number[b]=1
        print(number,parent)
        union_parent(parent,a,b)
        print(number,parent)
    # dic={}
    # arr=[]
    # cnt=0
    # for j in range(int(input())):
    #     p1,p2 =map(str,input().split())
    #     print(p1,p2)
    #     if p1 not in dic:
    #         dic[p1]=cnt
    #         cnt+=1
    #     if p2 not in dic:
    #         dic[p2]=cnt
    #         cnt+=1
    #     arr.append([p1,p2])
    # parent =[0]*(len(dic))
    # for i in range(len(parent)):
    #     parent[i]=i
    #
    # for p1,p2 in arr:
    #     print(dic[p1],dic[p2])
    #     print(parent)
    #     union_parent(parent,dic[p1],dic[p2])