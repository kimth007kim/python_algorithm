import sys

input =sys.stdin.readline

n,m= map(int,input().split())
arr= list(map(int,input().split()))

start=0
end= max(arr)
answer=0

while start<=end:
    total = 0
    mid = (start+end)//2
    if mid==0:
        total=0
        break

    for i in arr:
        if i >=mid:
            total+= i//mid

    if total>=n:
        answer= mid
        start= mid+1
    else:
        end= mid-1

# if answer==0:
#     print(-1)
# else:
print(answer)