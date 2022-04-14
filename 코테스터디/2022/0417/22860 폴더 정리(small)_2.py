parent={}
counter={}

def parent_plus(counter,parent,x,target):
    # print(x,target)
    if x==parent[x]:
        counter[x].append(target)
        return
    counter[x].append(target)
    parent_plus(counter,parent,parent[x],target)
answer=[]
folder, file = map(int,input().split())

counter= {}
arr=[]

for i in range(file+folder):
    p,c,type= input().split()

    if p not in counter:
        counter[p]=[]
    if c not in counter and type =="1":
        counter[c]=[]
    if p not in parent:
        parent[p]=p
    if c not in parent and type =="1":
        parent[c]=c

    if type=="0":
        # print("파일일 경우에")
        parent_plus(counter, parent, p, c)
    if type=="1":
        # print("폴더일 경우에")
        parent[c]=p
        for j in counter[c]:
            parent_plus(counter, parent,p, j)

for i in range(int(input())):
    tmp= list(input().split("/"))[-1]
    a,b= len(list(set(counter[tmp]))),len(counter[tmp])
    answer.append([a,b])

for a,b in answer:
    print(a,b)

