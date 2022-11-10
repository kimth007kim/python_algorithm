import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


def convert(number):
    result = 1
    m, k = 0, 0
    for i in number:
        if i == "K":
            k += 1
        if i == "M":
            m += 1
    result = result * (10 ** (len(number) - 1))
    if k == 1:
        result *= 5
    return str(result)

arr = list(input().rstrip())
length = len(arr)
maximum = ""
now = 0
while now < len(arr):
    for i in range(now, length):
        end = i + 1
        if arr[i] == "K":
            break
    tmp = arr[now:end]
    if end == len(arr) and  "K" not in tmp:
        for j in range(len(tmp)):
            maximum+="1"
    else:
        maximum += convert(tmp)
    now = end
    # break
print(maximum)

minimum = ""
now = 0
while now < len(arr):
    if arr[now] == "M":
        for i in range(now, length):
            end = i
            if arr[i] == "K":
                end -= 1
                break
        tmp = arr[now:end + 1]
        minimum += convert(tmp)
        now = end + 1
    else:
        minimum += "5"
        now += 1
print(minimum)
