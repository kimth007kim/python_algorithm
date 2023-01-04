import sys
input =sys.stdin.readline

n,k= map(int,input().split())

length = 1000000
arr= [0]*(length+1)
for i in range(n):
    g,x = map(int,input().split())
    start= max(0,x-k)
    end = min(length-1,x+k)
    arr[start]+=g
    arr[end+1]-=g

MAX=arr[0]
for i in range(1,len(arr)):
    arr[i]+=arr[i-1]
    MAX=max(arr[i],MAX)

print(MAX)
