from collections import deque
import sys


input =sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

n, m = map(int, input().split())
arr = []

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])

arr.sort(key=lambda x: x[0])
total = 0

q = deque(arr)
answer=[]
last=0
while q:
    dist, a, b = q.popleft()
    if find_parent(a,parent)!= find_parent(b,parent):
        union_parent(a,b,parent)
        total+=dist
        last=dist
        answer.append(dist)
        # print(a,b,dist,total)
# print(sum(answer[:-1]))

print(total-last)