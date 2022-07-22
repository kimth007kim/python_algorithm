from collections import deque
import sys

input =sys.stdin.readline

def plus_calc(arr):
    q = deque()
    result = 0
    for i in arr:
        q.append(i)

    while len(q) >= 2:
        a = q.popleft()
        b = q.popleft()
        # print(a,b)
        if a == 1 or b == 1:
            result += (a + b)
        else:
            result += (a * b)
    while q:
        t = q.popleft()
        result += t

    return result


n = int(input())

plus = []
minus = []
zero = []
for i in range(n):
    num = int(input())
    if num == 0:
        zero.append(num)
    elif num > 0:
        plus.append(num)
    else:
        minus.append(num)

answer = 0
minus.sort()
plus.sort(reverse=True)

# print(minus)
# if len(minus)==1
if len(minus) % 2 != 0:
    # 음수가 홀수개
    if len(zero) == 0:
        answer += plus_calc(minus)
    else:
        minus = minus[:-1]
        # print(minus)
        answer += plus_calc(minus)
else:
    answer += plus_calc(minus)
answer += plus_calc(plus)


print(answer)
