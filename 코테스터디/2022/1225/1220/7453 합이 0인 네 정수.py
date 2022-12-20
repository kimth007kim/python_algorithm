import sys
from collections import defaultdict

input = sys.stdin.readline

answer = 0

n = int(input())

graph = [[] for _ in range(4)]

front = []
back = []


for i in range(n):
    a, b, c, d = map(int, input().split())
    graph[0].append(a)
    graph[1].append(b)
    graph[2].append(c)
    graph[3].append(d)


ab = defaultdict(int)
for a in graph[0]:
    for b in graph[1]:
        v= a+b
        ab[v]+=1

for c in graph[2]:
    for d in graph[3]:
        v =-1 *(c+d)
        if v in ab:
            answer+=ab[v]

print(answer)