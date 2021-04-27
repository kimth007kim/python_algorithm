# 1~g번 까지 번호
# p개의 비행기가 차례대로 도착 예정
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

g=int(input())
p=int(input())

parent=[0]*(g+1)
for i in range(1,g+1):
    parent[i]=i


result=0

for i in range(p):
    data= find_parent(parent,int(input()))
    if data==0:
        break
    union_parent(parent,data,data-1)
    print(parent)
    result+=1

print(result)