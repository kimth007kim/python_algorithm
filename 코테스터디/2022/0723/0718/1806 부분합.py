import sys

input = sys.stdin.readline


n,s = map(int,input().split())
arr= list(map(int,input().split()))

LEN=int(1e11)
end= 0
start=0
prefix=0
while True:
    # print(start,end,prefix,LEN)
    if prefix>=s:
        LEN= min(LEN,(end-start))
        prefix-=arr[start]
        start+=1
    elif end==n:
        break
    else:
        prefix+=arr[end]
        end+=1



if LEN==int(1e11):
    print(0)
else:
    print(LEN)