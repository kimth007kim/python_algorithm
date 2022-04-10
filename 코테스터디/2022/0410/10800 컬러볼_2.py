import sys
input = sys.stdin.readline

n=int(input())

arr=[]

dic={}
cnt=0
MAX=0
for i in range(n):
    a,b= map(int,input().split())
    if a not in dic:
        dic[a]=cnt
        cnt+=1
    MAX=max(MAX,b)
    arr.append([a,b])

graph= [[0]*(MAX+2) for _ in range(len(dic))]

for a,b in arr:
    for i in dic:
        if i !=a:
            graph[dic[i]][b+1]+=b

for i in range(len(graph)):
    prev=0
    for j in range(1,len(graph[0])):
        graph[i][j]+=prev
        prev=graph[i][j]

answer=[]
for a,b in arr:
    answer.append(graph[dic[a]][b])

for i in answer:
    print(i)