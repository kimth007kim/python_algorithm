from collections import defaultdict,Counter
import sys

def input():
    return sys.stdin.readline().rstrip()
def dfs(position):

    temp = Counter(files[position])
    print()
    print("temp = ",temp)
    print("files = ",files)
    print(position,folders)
    for next_folder in folders[position]:
        print(next_folder)
        if next_folder not in delete_folder_name:
            temp+=dfs(next_folder)
    result[position]=[len(temp),sum(temp.values())]
    return temp


n, m = map(int, input().split())
folders= defaultdict(list)
files= defaultdict(set)
for _ in range(n+m):
    upper,lower,isFolder =input().split()
    if isFolder=='1':
        folders[upper].append(lower)
    else:
        files[upper].add(lower)

k = int(input())
delete_folder_name=set()
for _ in range(k):
    before,after=input().split()
    before_folder=before.split('/')[-1]
    after_folder=after.split('/')[-1]

    for folder_name in folders[before_folder]:
        folders[after_folder].append(folder_name)

    for file_name in files[before_folder]:
        files[after_folder].add(file_name)
    print(files)
    print(folders)
    folders[before_folder].clear()
    files[before_folder].clear()
    delete_folder_name.add(before_folder)

result={}
dfs("main")

q=int(input())

for _ in range(q):
    last_folder= input().split('/')[-1]
    print(*result[last_folder])