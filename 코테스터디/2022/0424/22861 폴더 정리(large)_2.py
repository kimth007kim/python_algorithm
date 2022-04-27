from collections import defaultdict,Counter


n,m = map(int,input().split())
result={}
folders=defaultdict(list)
files=defaultdict(set)
delete_folder=set()

def dfs(position):
    temp = Counter(files[position])
    print(position,temp,result)
    for next_folder in folders[position]:
        if next_folder not in delete_folder:
            temp+=dfs(next_folder)
    result[position]=[len(temp),sum(temp.values())]
    print(position,temp,result)
    return temp

for _ in range(n+m):
    upper,lower,file_or_folder = input().split()
    if file_or_folder=="1":
        folders[upper].append(lower)
    else:
        files[upper].add(lower)

for _ in range(int(input())):
    start,end = input().split()
    start = start.split("/")[-1]
    end = end.split("/")[-1]

    for i in folders[start]:
        folders[end].append(i)
    folders[start].clear()

    for i in files[start]:
        files[end].add(i)
    files[start].clear()
    delete_folder.add(start)


print("files",files)
print("folders",folders)
dfs("main")
answer= []