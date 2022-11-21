import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def score(num, flag):
    global target, non
    if flag == True:
        if num == 1:
            target += 1
        else:
            non += 1
    else:
        if num == 1:
            target -= 1
        else:
            non -= 1


# n, k = 10, 3
# arr = [1, 2, 2, 2, 1, 2, 1, 2, 2, 1]
# print(arr)

non = 0
target = 0
inf =int(1e11)
answer = inf
end = 0
for start in range(n):
    while end < n and target <k:
        score(arr[end], True)

        end += 1
        # print(start,end,answer)
        # print(target,non)
    if target==k:
        answer = min(answer, end - start)
    score(arr[start], False)
if answer==inf:
    print(-1)
else:
    print(answer)
