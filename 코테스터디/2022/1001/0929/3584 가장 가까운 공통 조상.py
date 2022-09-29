import sys

sys.setrecursionlimit(int(1e5))

def find_parents(x,arr):
    # print(x,arr)
    if x==-1 or parents[x]==-1:
        return
    if parents[x]!=-1 or x!=-1:
        arr.append(parents[x])
        find_parents(parents[x],arr)
        return
    return

t= int(input())
for _ in range(t):
    n= int(input())
    parents=[-1]*(n+1)
    for i in range(n-1):
        p,c = map(int,input().split())
        parents[c]=p
    a,b =map(int,input().split())
    arrA=[a]
    arrB=[b]
    find_parents(a,arrA)
    find_parents(b,arrB)
    MAX= max(len(arrA),len(arrB))
    if len(arrA)!=MAX:
        arrA= [0]*(len(arrB)-len(arrA))+arrA
    if len(arrB)!=MAX:
        arrB= [0]*(len(arrA)-len(arrB))+arrB
    # print(arrA,arrB)
    for i in range(MAX):
        if arrA[i]==arrB[i]:
            print(arrA[i])
            break