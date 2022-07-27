import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = 0
start = 0
cnt = int(1e9)
for end in range(len(arr)):
    prefix += arr[end]
    if prefix >= m:
        # print("end",end,"start",start,end-start)
        cnt = min(cnt, end - start + 1)
        while prefix >= m:
            prefix -= arr[start]
            start += 1
            if prefix >= m:
                cnt = min(cnt, end - start + 1)
                # print("end",end,"start",start,end-start)
    # print(start,end,prefix)
if cnt==int(1e9):
    print(0)
else:
    print(cnt)
