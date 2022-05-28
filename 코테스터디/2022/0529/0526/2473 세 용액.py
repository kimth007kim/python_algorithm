import sys


def two_pointer(now, arr):
    global MIN, answer_s, answer_e, answer_n
    start = now +1
    end = len(arr)-1

    # print("--------------------")
    # print("Start=",start,now,"end=",end)
    # print("--------------------")
    while start<=len(arr)-1 and end>=0:
    # while start >= 0 and end <= len(arr) - 1:
        Sum = arr[start] + arr[now] + arr[end]
        # print(start, end, Sum)
        tmp = abs(Sum)
        if tmp < MIN:
            MIN = tmp
            answer_s = arr[start]
            answer_n = arr[now]
            answer_e = arr[end]
        if Sum < 0:
            start += 1
        elif Sum > 0:
            end -= 1



# n=5
# arr=[-2, 6, -97, -6, 98]
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer_s = 0
answer_e = 0
answer_n = 0
MIN = 0

MIN = int(1e11)
for now in range(n - 2):
    two_pointer(now, arr)

print(answer_s, answer_n, answer_e)
