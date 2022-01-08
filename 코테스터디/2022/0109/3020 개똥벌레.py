# https://www.acmicpc.net/problem/3020

import sys
input =sys.stdin.readline

def show(arr):
    for i in arr:
        print(i)

def count(arr,number):
    total = sum(arr[number])
    return total
n,h =map(int,input().split())
end=h
graph = [ [0]*n for _ in range(h)]


for i in range(n):
    tmp = int(input())
    if i%2!=0:
        for j in range(tmp):
            graph[j][i]=1
    else:
        for j in range(h-1,h-tmp-1,-1):
            graph[j][i]=1
MIN=int(1e9)
cnt=0
for i in range(h):
    tmp = count(graph,i)

    if MIN>tmp:
        cnt=1
        MIN=tmp
    elif MIN==tmp:
        cnt+=1

print(MIN,cnt)