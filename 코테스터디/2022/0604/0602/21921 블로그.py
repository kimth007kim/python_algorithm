import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

start=0
end=x-1
SUM=sum(arr[start:end])
# print(SUM)
MAX=SUM
cnt=1
while end<n:
    SUM+=arr[end]
    # print(start,end)
    if SUM>MAX:
        MAX=SUM
        cnt=1
    elif SUM==MAX:
        cnt+=1
    # print(SUM)
    end+=1
    SUM-=arr[start]
    start+=1


if MAX==0:
    print("SAD")
else:
    print(MAX)
    print(cnt)