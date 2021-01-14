a=int(input())
b=int(input())

graph= [ [] for _ in range(a+1)]
visited=[False]* a
print(visited)
print(graph)

for i in range(b):
    c,d=map(int,input().split())