import sys

input =sys.stdin.readline

n= int(input())
m= int(input())

road = [0]*(n+1)
arr= list(map(int,input().split()))

start=0
end= n
answer=int(1e9)
while start<=end:
    mid = (start+end)//2
    road = [0]*(n+1)
    for i in arr:
        s = i-mid
        if s<0:
            s=0
        e = i+mid
        if e>n:
            e= n
        for j in range(s,e+1):
            road[j]=1

    if 0 in road:
        start=mid+1
    else:
        answer=min(answer,mid)
        end=mid-1
    # break

print(answer)