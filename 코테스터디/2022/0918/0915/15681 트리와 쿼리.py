import sys
sys.setrecursionlimit(10**5)
input =sys.stdin.readline



n,r,q = map(int,input().split())

def makeTree(now,parent):
    for node in graph[now]:
        if node != parent:
            child[now].append(node)
            parents[node]=now
            makeTree(node,now)

def countSubtreeNodes(now) :
    size[now] = 1
    for Node in child[now]:
        countSubtreeNodes(Node)
        size[now] += size[Node]

graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
query = []



parents=[0]*(n+1)
# parents[r]=-1
child=[[] for  _ in range(n+1)]
size=[0]*(n+1)

makeTree(r,-1)
countSubtreeNodes(r)
for i in range(q):
    target = int(input())
    print(size[target])
# makeTree(r,parent)