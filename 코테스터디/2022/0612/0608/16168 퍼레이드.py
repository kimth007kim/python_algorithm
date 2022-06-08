from collections import defaultdict

def result(parents,road):
    prev= find(parents,1)
    for i in range(2,len(parents)):
        if prev != find(parents,i):
            return "NO"

    # print(parents,road)
    odd=0
    for i in road:
        length = len(road[i])%2
        if length!=0:
            odd+=1
    if odd==0 or odd ==2:
        return "YES"

    return "NO"

def find(parents,x):
    if parents[x]!=x:
        parents[x]=find(parents,parents[x])
    return parents[x]

def union(a,b,parents):
    a= find(parents,a)
    b= find(parents,b)

    if a>b:
        parents[a]=b
    else:
        parents[b]=a

road=defaultdict(list)
v,e = map(int,input().split())
parents=[0]*(v+1)
for i in range(1,v+1):
    parents[i]=i
for i in range(e):
    a,b= map(int,input().split())
    road[a].append(b)
    road[b].append(a)
    union(a,b,parents)


print(result(parents,road))