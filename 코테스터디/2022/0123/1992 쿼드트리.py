# https://www.acmicpc.net/problem/1992


from collections import deque
# import sys
# input = sys.stdin.readline


def divide(graph,full):
    global word
    if full // 2 >0:
        array=[]
        half=len(graph)//2

        arr1 = []
        tmp=""
        for i in range(half):
            arr2=[]
            for j in range(half):
                tmp+=graph[i][j]
                arr2.append(graph[i][j])
            arr1.append(arr2)

        if len(set(tmp))!=1:

            return divide(arr1,half)
        else:
            word+=tmp[0]
        print(array)


def check_arr(arr):
    LENGTH= len(arr)
    first=arr[0][0]
    for i in range(LENGTH):
        for j in range(LENGTH):
            if arr[i][j]!= first:
                return False
    return True

n= int(input())

graph = []
for i in range(n):
    kk= list(map(str,input().strip()))
    graph.append(kk)
word=""
print(word)
if check_arr(graph):
    if graph[0][0]=="1":
        print("(1)")
    else:
        print("(0)")
else:
    q=deque()
    word=""
    word+=divide(graph,len(graph))
