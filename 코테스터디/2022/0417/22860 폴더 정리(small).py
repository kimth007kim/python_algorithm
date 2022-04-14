from collections import defaultdict
import sys
# input = sys.stdin.readline

parent={}
counter={}

def parent_plus(counter,parent,x,target):
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
    if c not in parent and type=="1":
        parent[c]=p
        # print(parent)
    if type=="0":
        parent_plus(counter, parent, p, c)
    print(p,c,counter)

# for i in range(int(input())):
#     tmp= list(input().split("/"))[-1]
#     print(counter)
#     # print(tmp)
#     a,b= len(list(set(counter[tmp]))),len(counter[tmp])
#     answer.append([a,b])
#
# for a,b in answer:
#     print(a,b)

