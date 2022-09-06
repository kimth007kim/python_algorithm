import sys

input =sys.stdin.readline

n= int(input())

arr= list(map(int,input().split()))
x= int(input())



# print(arr)
arr.sort()
# print(arr)

start=0
end=n-1
total=0
cnt=0
for start in range(n):
    total = arr[start] + arr[end]
    # print(start,end,total)
    if total==x:
        cnt+=1
    while end>=0 and total>=x:
        end-=1
        total =arr[start]+arr[end]
        if total == x:
            cnt += 1

print(cnt//2)
