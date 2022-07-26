import sys

input =sys.stdin.readline

n= int(input())
tmp= list(map(int,input().split()))
arr=[0]+tmp
for i in range(1,n+1):
    arr[i]+=arr[i-1]
# print(arr)
m = int(input())
val = []
for i in range(m):
    a,b = map(int,input().split())
    print(arr[b]-arr[a-1])