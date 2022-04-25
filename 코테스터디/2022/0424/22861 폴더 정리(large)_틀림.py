from collections import defaultdict

def move_parent(start,end,folders,parents):
    a=find_name(start)
    b=find_name(end)
    for i in parents:
        if parents[i]==a:
            parents[i]=b
    for i in folders[a]:
        folders[b].add(i)
    del folders[a]
    del parents[a]
    del file[a]
    # print(a,b)
    # print(folders)
    # print(parents)
    # print()

def find_name(word):
    arr= list(map(str,word.split("/")))
    return arr[-1]

def find_parents(now,components):
    file[now].append(components)
    if parents[now]!=now:
        find_parents(parents[now],components)



n,m= map(int,input().split())
parents={}
folders= defaultdict(set)
file= defaultdict(list)

for i in range(n+m):
    p,c,types=map(str,input().split())
    if p not in parents:
        file[p]
        parents[p]=p
        folders[p]
    if types=="1":
        if c not in parents:
            folders[c]
            file[c]
            parents[c]=p
    else:
        folders[p].add(c)
# print(folders)
# print(parents)
# print()
for _ in range(int(input())):
    start,end = map(str,input().split())
    move_parent(start,end,folders,parents)

for now in parents:
    for i in folders[now]:
        find_parents(now,i)


answer=[]
for _ in range(int(input())):
    query = input()
    target=find_name(query)
    answer.append([len(list(set(file[target]))),len(file[target])])

for i in answer:
    print(*i)