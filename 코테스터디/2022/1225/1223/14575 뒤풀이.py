import sys

input =sys.stdin.readline
def binary_search(start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        total = 0
        correct = 0
        small=0
        big=0
        # print(mid,total,correct)
        # if mid *
        for i in range(n):
            if MIN[i] <= mid <= MAX[i]:
                total += max(mid, MIN[i])
                correct += 1
                small+=min(mid,MIN[i])
                big+=min(MAX[i],mid)

            elif MAX[i] <= mid:
                # print(MIN[i],MAX[i],mid)
                total += MAX[i]
                correct += 1
                small+=MIN[i]
                big+=MAX[i]
            # print(mid,"  ", total)
        if total < t or correct != n:
            start = mid + 1
        else:
            # print("큰값")
            if small<=t<=big:
                answer = min(mid, answer)
            end = mid - 1
        # break


flag = False

n, t = map(int, input().split())
MIN = []
MAX = []
INF= int(1e15)
answer = INF
# print(n, t)
for i in range(n):
    a, b = map(int, input().split())
    MIN.append(a)
    MAX.append(b)

s, e = min(MIN), max(MAX)

# print(s,e)
binary_search(s, e)
if answer!= INF:
    print(answer)
else:
    print(-1)
