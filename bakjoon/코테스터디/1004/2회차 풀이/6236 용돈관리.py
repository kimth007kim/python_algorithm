import sys
input = sys.stdin.readline


n,m= map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

start=min(arr)
end=sum(arr)


while start<=end:
    mid = (start+end)//2
    total=mid
    cnt=1
    for i in arr:
        if i>total:
            cnt+=1
            total=mid
        total-=i
    if cnt>m or mid<max(arr):
        start = mid + 1
    else:
        end= mid-1
        k= mid

print(k)