import sys
from collections import defaultdict

input =sys.stdin.readline

answer=0


def dfs(now,total,graph):

    global answer
    if now==3:
        need = -total
        if need in dic:
            answer+=1
        return
    for i in graph[now]:
        dfs(now+1,total+i,graph)



n= int(input())


graph=[[] for _ in range(3)]
dic= defaultdict(int)


for i in range(n):
    a1,b1,c1,d1 = map(int,input().split())
    graph[0].append(a1)
    graph[1].append(b1)
    graph[2].append(c1)
    dic[d1]+=1

for i in range(n):
    dfs(1,graph[0][i],graph)

print(answer)