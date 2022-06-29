from collections import defaultdict
n= int(input())

x,y = map(int,input().split())
dx= defaultdict(list)
dy= defaultdict(list)
arr = []
answer=0
for i in range(n):
    a,b = map(int,input().split())
    dx[a].append(b)
    dy[b].append(a)
    arr.append([a,b])
for a,b in arr:
    if b+y not in dx[a]:
        continue
    if a+x not in dy[b]:
        continue
    if b+y not in dx[a+x]:
        continue
    answer+=1
print(answer)