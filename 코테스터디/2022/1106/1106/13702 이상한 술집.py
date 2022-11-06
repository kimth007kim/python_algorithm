import sys

input = sys.stdin.readline


def binary(start, end, target):
    global answer
    while start <= end:
        mid = (start + end) // 2
        cup = 0
        for i in arr:
            cup += i // mid

        # print(mid,cup)
        if cup >= target:
            start = mid+1
            answer = max(answer, mid)

        else:
            end = mid - 1
        # if cup==target:


answer = 0
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

binary(1, max(arr), m)
print(answer)
