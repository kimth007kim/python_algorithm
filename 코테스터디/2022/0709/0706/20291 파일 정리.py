import sys

input = sys.stdin.readline

n= int(input())


file={}
arr=[]
for i in range(n):
    name,ex = map(str,input().rstrip().split("."))
    if ex not in file:
        arr.append(ex)
        file[ex]=[]
    file[ex].append(name)
arr.sort()

for i in arr:
    print(i,len(file[i]))


