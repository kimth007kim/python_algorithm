import sys

input=sys.stdin.readline

def bs(start, end,now):
    global answer,MIN
    while start<=end:
        mid = (start + end) // 2
        origin=arr[mid] + arr[now]
        target = abs(origin - m)

        if target < MIN:
            MIN = target
            answer = 1
        elif target == MIN:
            answer += 1

        if origin>m:
            end=mid-1
        else:
            start=mid+1




t = 1
t=int(input())
for i in range(t):
    n,m= map(int,input().split())
    arr=list(map(int,input().split()))
    # n, m = 10, 8
    # arr = [-7, 9, 2, -4, 12, 1, 5, -3, -2, 0]
    answer=0
    MIN=int(1e11)
    arr.sort()
    # print(arr)





    for now in range(len(arr)):
        bs(now+1,len(arr)-1,now)
    print(answer)
