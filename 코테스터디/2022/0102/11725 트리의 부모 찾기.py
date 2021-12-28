import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n= int(input())

tree = [[] for _ in range(n+1)]
parents=[0 for _ in range(n+1)]

print(tree)
print(parents)

for _ in range(n-1):
    a,b= map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)
print(parents)

def dfs(start,tree,parents):
    print(start,tree,parents)
    for i in tree[start]:
        if parents[i]== 0:
            parents[i]=start
            dfs(i,tree,parents)

dfs(1,tree,parents)