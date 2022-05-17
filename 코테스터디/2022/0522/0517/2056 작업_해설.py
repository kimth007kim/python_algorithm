from collections import defaultdict
import sys

input = sys.stdin.readline

n= int(input())
times=[0]*(n+1)
graph=defaultdict(list)
for i in range(1,n+1):
    lst = list(map(int,input().split()))
    times[i]= lst[0]
    if lst[1]==0:
        continue
    for j in lst[2:]:
        graph[i].append(j)

for i in range(1,n+1):
    if i in graph:
        time =0
        for j in graph[i]:
            time = max(time,times[j])
            print(i,time)
        print()
        times[i]+=time
        print(times)

print(times)
print(graph)