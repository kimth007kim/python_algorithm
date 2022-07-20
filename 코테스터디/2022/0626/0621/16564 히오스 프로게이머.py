import sys

input =sys.stdin.readline

def count(arr,m):
    t=0
    for n in arr:
        if n>=m:
            break
        t+=m-n
    return t

n,k = map(int,input().split())
arr= []
for i in range(n):
    tmp = int(input())
    # print(tmp)
    arr.append(tmp)

arr.sort()

start=arr[0]
end=arr[n-1]+k
MAX=arr[0]

while start<=end:
    mid = (start+end)//2
    total=k
    if count(arr,mid)<=k:
        MAX= mid
        start =mid+1
    else:
        end = mid-1

    # if total==0:
    #     MAX= max(MAX,mid)
    # if total>0:
    #     start= mid+1
    #     MAX= max(MAX,mid)
    # if total<0:
    #     end = mid-1

print(MAX)


