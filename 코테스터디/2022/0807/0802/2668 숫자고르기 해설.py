import sys

input = sys.stdin.readline
def dfs(v,i):
    visited[v]=True
    print(v,i)
    for w in arr[v]:
        if not(visited[w]):
            dfs(w,i)
        elif visited[w] and w==i:
            print("---",w,i)
            result.append(w)
            print(result)

n = int(input())
arr = [[] for _ in range(n+1)]
print(arr)

for i in range(n):
    arr[i+1].append(int(input()))

result = []
print(arr)
for i in range(1,n+1):
    visited= [False] *(n+1)
    dfs(i,i)
    print(visited)