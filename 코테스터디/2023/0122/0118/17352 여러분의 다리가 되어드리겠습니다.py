import sys

input =sys.stdin.readline

def find(x):
    if parents[x]!=x:
        return find(parents[x])
    return parents[x]

def union(a,b):
    a,b = find(a),find(b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a

n = int(input())
parents=[i for i in range(n+1)]

# print(parents)
for i in range(n-2):
    a,b = map(int,input().split())
    union(a,b)
    # print(parents)
answer=set()
for i in range(1,n+1):
    t= find(i)
    answer.add(t)
answer= list(answer)
print(*answer)