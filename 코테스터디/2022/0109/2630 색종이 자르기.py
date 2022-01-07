# https://www.acmicpc.net/problem/2630
import sys
from collections import deque

input = sys.stdin.readline

def check(arr):
    first = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if first != arr[i][j]:
                return -1
    return first


def divide(q, graph, length, next):
    global zero, one
    arr = []
    for i in range(next):
        tmp = []
        for j in range(next):
            tmp.append(graph[i][j])
        arr.append(tmp)

    if check(arr) == -1:
        q.append(arr)
    elif check(arr) == 0:
        zero += 1
    else:
        one += 1

    arr = []
    for i in range(next):
        tmp = []
        for j in range(next, length):
            tmp.append(graph[i][j])
        arr.append(tmp)

    if check(arr) == -1:
        q.append(arr)
    elif check(arr) == 0:
        zero += 1
    else:
        one += 1

    arr = []
    for i in range(next, length):
        tmp = []
        for j in range(next):
            tmp.append(graph[i][j])
        arr.append(tmp)

    if check(arr) == -1:
        q.append(arr)
    elif check(arr) == 0:
        zero += 1
    else:
        one += 1

    arr = []
    for i in range(next, length):
        tmp = []
        for j in range(next, length):
            tmp.append(graph[i][j])
        arr.append(tmp)

    if check(arr) == -1:
        q.append(arr)
    elif check(arr) == 0:
        zero += 1
    else:
        one += 1


n= int(input())
graph= []
for i in range(n):
    graph.append(list(map(int,input().split())))


zero = 0
one = 0

cnt=n*n
num=0
first = graph[0][0]
for i in range(n):
    for j in range(n):
        if first==graph[i][j]:
            num+=1
if cnt==num:
    if first==0:
        print(1)
        print(0)
    else:
        print(0)
        print(1)
else:
    q = deque()
    q.append(graph)
    while q:
        tmp = q.popleft()
        divide(q, tmp, len(tmp), len(tmp) // 2)

    print(zero)
    print(one)