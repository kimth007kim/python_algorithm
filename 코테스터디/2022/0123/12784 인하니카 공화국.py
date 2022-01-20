# https://www.acmicpc.net/problem/12784


def tracking(graph,num):
    if len(graph)==0:
        print(num)
        return
    for i in graph[num]:
        tracking(graph,i[0])

t=  int(input())
v,e = map(int,input().split())



graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b,distance= map(int,input().split())
    graph[a].append([b,distance])
    graph[b].append([a,distance])
# print(graph)
cand=[]

for i in range(v+1):
    if len(graph[i])==1:
        # print(i)
        cand.append(i)

# print(cand)

tracking(graph,1)