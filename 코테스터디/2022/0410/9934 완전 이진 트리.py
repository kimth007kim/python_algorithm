import sys
input = sys.stdin.readline

k= int(input())
_input = list(map(int,input().split()))
print(_input)
tree= [[] for _ in range(k)]
def makeTree(arr,x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    print(tree,arr,x)
    print(" -- ",arr[:mid],arr[mid+1:])
    if len(arr)==1:
        return
    makeTree(arr[:mid],x+1)
    makeTree(arr[mid+1:],x+1)



makeTree(_input,0)
for i in range(k):
    print(*tree[i])