import sys

input = sys.stdin.readline
n = int(input())
graph= [ [ ] for _ in range(n+1)]
vertex = []
for i in range(n - 1):
    a, b = map(int, input().split())
    vertex.append([a, b])
    graph[a].append(b)
    graph[b].append(a)

m = int(input())
for i in range(m):
    a,b= map(int,input().split())
    # 1일때 단절점
    if a == 1:
        if len(graph[b])==1:
            print("no")
        else:
            print("yes")
    else:
        print("yes")