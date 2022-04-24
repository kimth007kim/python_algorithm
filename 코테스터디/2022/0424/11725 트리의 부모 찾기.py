import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())

tree= [[] for _ in range(n+1)]

parents=[0 for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start,tree,parents):
    print(start)
    for i in tree[start]:
        if parents[i]==0:
            parents[i]=start
            print(i,parents)
            DFS(i,tree,parents)

DFS(1,tree,parents)